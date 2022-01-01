# update_plot.py
from TemperatureMeasurement import sub
from datetime import datetime, date, time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import queue
import time
import sys
import csv
import os


# initial the global var.
payload = bytes()
temperature_list = []
temperature_array = np.array("")


def write_csv():
    # receive data from sub.py
    sub.run_sub()
    global payload
    global temperature_list
    global temperature_array
    payload = sub.payload
    if payload == bytes():
        pass  # if payload is empty, then pass
    else:
        temperature_list = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace(
            "]", "").split(",")  # reform the temperature list
        temperature_array = np.array(temperature_list).reshape(
            (24, 32))  # convert the temperature list into a 24x32 array


temperature_array_shape = np.shape(temperature_array)  # mlx90640 shape
interp_val = 1  # no interpolation
interp_shape = (24 * interp_val,
                32 * interp_val)  # new shape


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

# frame = np.zeros(mlx_shape[0] * mlx_shape[1])  # 768 pts

print(type(temperature_array))
def plot_update():
    fig_pc.canvas.restore_region(ax_background)  # restore background

    therm1.set_array(temperature_array)  # set data
    therm1.set_clim(vmin=np.min(temperature_array), vmax=np.max(temperature_array))  # set bounds
    cbar.update_normal(therm1) # update colorbar range (new version)

    ax.draw_artist(therm1)  # draw new thermal image
    fig_pc.canvas.blit(ax.bbox)  # draw background
    fig_pc.canvas.flush_events()  # show the new image


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

plot_update()