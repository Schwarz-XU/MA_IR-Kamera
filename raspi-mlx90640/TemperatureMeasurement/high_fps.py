##########################################
# MLX90640 Thermal Camera w Raspberry Pi
# -- 2fps with Interpolation and Blitting
##########################################
#
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
from scipy import ndimage
from TemperatureMeasurement import pub


# establish I2C bus
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)  # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c)  # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ # set refresh rate
mlx_shape = (24, 32)  # mlx90640 shape
mlx_interp_val = 10  # interpolate # on each dimension
mlx_interp_shape = (mlx_shape[0]*mlx_interp_val,
                    mlx_shape[1]*mlx_interp_val)  # new shape

# set plot
fig = plt.figure(figsize=(12, 9))  # start figure
ax = fig.add_subplot(111)  # add subplot
fig.subplots_adjust(0.05, 0.05, 0.95,  0.95) # get rid of unnecessary padding
therm1 = ax.imshow(np.zeros(mlx_interp_shape), interpolation='none',
                   cmap=plt.cm.bwr, min=25, vmax=45)  # preemptive image
# temperature scale
cbar = fig.colorbar(therm1)  # setup colorbar
cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label

fig.canvas.draw()  # draw figure to copy background
ax_background = fig.canvas.copy_from_bbox(ax.bbox)  # copy background
fig.show()  # show the figure before blitting

frame = np.zeros(mlx_shape[0]*mlx_shape[1])  # 768 pts


def plot_update():
    fig.canvas.restore_region(ax_background)  # restore background
    mlx.getFrame(frame) # read mlx90640
    data_array_raw = np.fliplr(np.reshape(frame, mlx_shape))  # reshape, flip data
    data_array_raw[23][31] = (data_array_raw[22][31]
                              + data_array_raw[23][30]
                              + data_array_raw[22][30]) / 3  # fix error pixel with the average value of nearest
    data_array_raw = ndimage.zoom(data_array_raw, mlx_interp_val)  # interpolate
    therm1.set_array(data_array_raw)  # set data
    therm1.set_clim(vmin=np.min(data_array_raw), vmax=np.max(data_array_raw))  # set bounds
    cbar.on_mappable_changed(therm1)  # update colorbar range

    ax.draw_artist(therm1)  # draw new thermal image
    fig.canvas.blit(ax.bbox)  # draw background
    fig.canvas.flush_events()  # show the new image
    return data_array_raw


t_array = []
while True:
    t1 = time.monotonic()  # for determining frame rate
    try:
        plot_update()  # update plot
        data_array_raw = plot_update()
        publisher = pub.publisher
        publisher.publish(data_array_raw)
    except:
        continue
    # approximating frame rate
    t_array.append(time.monotonic()-t1)
    if len(t_array) > 10:
        t_array = t_array[1:]  # recent times for frame rate approx
    print('Frame Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
