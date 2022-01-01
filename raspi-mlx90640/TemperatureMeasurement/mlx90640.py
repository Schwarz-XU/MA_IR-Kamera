"""
# MLX90640 Thermal Camera with Raspberry Pi
# -- 2fps with Interpolation and Blitting
"""

import board
import busio
import time
import adafruit_mlx90640
import numpy as np
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
from scipy import ndimage

# establish I2C bus
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)  # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c)  # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ  # set refresh rate
# mlx90640 build
mlx_shape = (24, 32)  # mlx90640 shape
# mlx_interp_val = 10  # interpolate (on each dimension)
mlx_interp_val = 1  # no interpolation
mlx_interp_shape = (mlx_shape[0] * mlx_interp_val,
                    mlx_shape[1] * mlx_interp_val)  # new shape


# set plot
fig = plt.figure(figsize=(12, 9))  # start figure
ax = fig.add_subplot(111)  # add subplot
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95)  # get rid of unnecessary padding
therm1 = ax.imshow(np.zeros(mlx_interp_shape), interpolation='none',
                   cmap=plt.cm.bwr, vmin=25, vmax=45)  # preemptive image
# temperature scale
cbar = fig.colorbar(therm1)  # setup colorbar
cbar.set_label('Temperature [$^{\circ}$C]', fontsize=14)  # colorbar label

fig.canvas.draw()  # draw figure to copy background
ax_background = fig.canvas.copy_from_bbox(ax.bbox)  # copy background
# fig.show()  # show the figure before blitting

frame = np.zeros(mlx_shape[0] * mlx_shape[1])  # 768 pts


def plot_update():
    fig.canvas.restore_region(ax_background)  # restore background
    mlx.getFrame(frame)  # read mlx90640
    data_array_raw = np.fliplr(np.reshape(frame, mlx_shape))  # reshape, flip data
    data_array_raw[23][31] = (data_array_raw[22][31]
                              + data_array_raw[23][30]
                              + data_array_raw[22][30]) / 3  # fix error pixel with the average value of nearst
    data_array_raw = ndimage.zoom(data_array_raw, mlx_interp_val)  # interpolate
    therm1.set_array(data_array_raw)  # set data
    therm1.set_clim(vmin=np.min(data_array_raw), vmax=np.max(data_array_raw))  # set bounds
    # cbar.on_mappable_changed(therm1)  # old version of function
    cbar.update_normal(therm1) # update colorbar range (new version)

    ax.draw_artist(therm1)  # draw new thermal image
    fig.canvas.blit(ax.bbox)  # draw background
    fig.canvas.flush_events()  # show the new image
    return data_array_raw


# TODO: try to not show die figure to improve the program efficiency
'''
frame = np.zeros(mlx_shape[0] * mlx_shape[1])  # 768 pts
data_array_raw = np.fliplr(np.reshape(frame, mlx_shape))  # reshape, flip data
data_array_raw[23][31] = (data_array_raw[22][31]
                            + data_array_raw[23][30]
                            + data_array_raw[22][30]) / 3  # fix error pixel before
data_array_raw = ndimage.zoom(data_array_raw, mlx_interp_val)  # interpolate
print(data_array_raw)
'''


# publisher
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    

# establish connection
client = mqtt.Client()
# client = mqtt.Client(client_id="mqttx_test")
client.username_pw_set(username="UEl-Rkl_Tm", password="12345678")  # TODO: not usable, need correction
client.on_connect = on_connect
client.will_set("raspberry/pub/status", b'{"status": "off"}') # Set will to find the status of raspberry pi
client.connect("broker.emqx.io", 1883, 60)  # TODO: free server right now, replace it with institute's server later

t_array = []

while True:
    t1 = time.monotonic()  # for determining frame rate
    try:
        plot_update()  # update plot
        data_array_raw = plot_update()

        # send all data_array to the broker
        data_array_str = np.array2string(data_array_raw, precision=2, separator=",", formatter={'float_kind':lambda x: "%.2f"% x})
        client.publish('raspberry/temperature_array', payload=data_array_str, qos=0, retain=False)
        print(f"send {data_array_str} to raspberry/temperature_array")
    except:
        continue

    # approximating frame rate
    t_array.append(time.monotonic() - t1)
    if len(t_array) > 10:
        t_array = t_array[1:]  # recent times for frame rate approx
    print('Frame Rate: {0:2.1f}fps'.format(len(t_array) / np.sum(t_array)))
    