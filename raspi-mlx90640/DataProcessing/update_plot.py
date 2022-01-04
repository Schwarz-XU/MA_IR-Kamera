# update_plot.py
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath("../"))
from TemperatureMeasurement import sub


temperature_array_shape = (24, 32)  # mlx90640 shape
interp_val = 1  # no interpolation
interp_shape = (temperature_array_shape[0] * interp_val,
            temperature_array_shape[1] * interp_val)  # new shape

# initial the global var.
payload = bytes()
temperature_list = []
temperature_array = np.array("")


def access_data():
    # receive data from sub.py
    sub.run_sub()
    global payload
    global temperature_list
    global temperature_array
    payload = sub.payload

    # set plot
    fig_pc = plt.figure(figsize=(12, 9))  # start figure
    ax = fig_pc.add_subplot(111)  # add subplot
    fig_pc.subplots_adjust(0.05, 0.05, 0.95, 0.95)  # get rid of unnecessary padding
    therm1 = ax.imshow(np.zeros(interp_shape), interpolation='none',
                       cmap=plt.cm.bwr, vmin=25, vmax=45)  # preemptive image
    # temperature scale
    cbar = fig_pc.colorbar(therm1)  # setup colorbar
    cbar.set_label('Temperature [$^{\circ}$C]', fontsize=14)  # colorbar label

    fig_pc.canvas.draw()  # draw figure to copy background
    ax_background = fig_pc.canvas.copy_from_bbox(ax.bbox)  # copy background
    fig_pc.show()  # show the figure before blitting
    # frame = np.zeros(24 * 32)  # 768 pts
    if payload == bytes():
        pass
    else:
        temperature_list = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace(
            "]", "").split(",")  # reform the temperature list
        temperature_array = np.array(temperature_list).reshape(
            (24, 32))  # convert the temperature list into a 24x32 array
        print(temperature_array)
        fig_pc.canvas.restore_region(ax_background)  # restore background
        # temperature_array = np.fliplr(np.reshape(frame, (24, 32)))  # reshape, flip data
        # temperature_array = ndimage.zoom(temperature_array, interp_val)
        therm1.set_array(temperature_array)  # set data
        print("this is running")
        therm1.set_clim(vmin=np.min(temperature_array), vmax=np.max(temperature_array))  # set bounds
        cbar.update_normal(therm1)  # update colorbar range (new version)
        ax.draw_artist(therm1)  # draw new thermal image
        fig_pc.canvas.blit(ax.bbox)  # draw background
        fig_pc.canvas.flush_events()  # show the new image


'''

def plot_update():
    access_data()
    fig_pc.canvas.restore_region(ax_background)  # restore background
    global temperature_array
    # temperature_array = np.fliplr(np.reshape(frame, (24, 32)))  # reshape, flip data
    # temperature_array = ndimage.zoom(temperature_array, interp_val)
    therm1.set_array(temperature_array)  # set data
    print("this is running")
    therm1.set_clim(vmin=np.min(temperature_array), vmax=np.max(temperature_array))  # set bounds
    cbar.update_normal(therm1)  # update colorbar range (new version)
    ax.draw_artist(therm1)  # draw new thermal image
    fig_pc.canvas.blit(ax.bbox)  # draw background
    fig_pc.canvas.flush_events()  # show the new image
'''

while True:
    try:
        access_data()
    except:
        continue
