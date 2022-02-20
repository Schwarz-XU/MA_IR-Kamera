# ir_camera_pc.py
import time 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib; matplotlib.use("TkAgg")
from scipy import ndimage
from DataAcquisition import sub
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


interp_val = 20  # interpolation
# create the figure
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95)

# creat a customized colormap
clist = ["blue", "lime", "lime", "yellow", "red"]
newcmp = LinearSegmentedColormap.from_list("therm", clist)

# therm = ax.imshow(np.zeros((24, 32)), interpolation='none', cmap="jet", vmin=25, vmax=45, animated=True)
therm = ax.imshow(np.zeros((24, 32)), interpolation='none', cmap=newcmp, vmin=25, vmax=45, animated=True)
# set a color_scale
color_scale = fig.colorbar(therm)
color_scale.set_label('Temperature [$^{\circ}$C]', fontsize=11)
# start to draw
fig.canvas.draw()  # draw figure to copy background
ax_background = fig.canvas.copy_from_bbox(ax.bbox)  # copy background
fig.show()
frame = np.zeros(768)  # initial pixel number of mlx90640


# initial global var.
# temperature_array = np.array([])


def data_access():
    sub.run()
    temperature_array = sub.temperature_array
    return temperature_array


def update_plot(temperature_data):
    fig.canvas.restore_region(ax_background)
    data_interp = ndimage.zoom(temperature_data, interp_val)
    therm.set_array(data_interp)
    therm.set_clim(vmin=np.min(data_interp), vmax=np.max(data_interp))
    color_scale.update_normal(therm)

    ax.draw_artist(therm)
    fig.canvas.blit(ax.bbox)
    fig.canvas.flush_events()


def run():
    t_array = []
    while True:
        t1 = time.monotonic()  # for determining frame rate
        try:
            data = data_access()
            if data.size > 0:
                update_plot(data)
            else:
                continue
        except Exception as e:
            print(repr(e))
            break
        t_array.append(time.monotonic() - t1)
        if len(t_array) > 10:
            t_array = t_array[1:]  # recent times for frame rate approx
        print('Frame Rate: {0:2.1f}fps'.format(len(t_array) / np.sum(t_array)))


if __name__ == '__main__':
    run()
