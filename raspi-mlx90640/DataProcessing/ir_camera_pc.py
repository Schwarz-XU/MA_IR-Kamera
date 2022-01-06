# ir_camera_pc.py
import time
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from DataAcquisition import sub


interp_val = 20  # interpolation
# create the figure
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111)
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95)
therm = ax.imshow(np.zeros((24, 32)), interpolation='none', cmap=plt.cm.bwr, vmin=25, vmax=45, animated=True)
# set a color_scale
color_scale = fig.colorbar(therm)
color_scale.set_label('Temperature [$^{\circ}$C]', fontsize=11)
# start to draw
fig.canvas.draw()  # draw figure to copy background
ax_background = fig.canvas.copy_from_bbox(ax.bbox)  # copy background
fig.show()
frame = np.zeros(768)

# initial global var.
temperature_array = np.array([])


def data_access():
    sub.run()
    data_payload = sub.payload
    global temperature_array
    if data_payload == bytes():
        print("the data_payload is empty")
        pass
    else:
        temperature_list_str = str(data_payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace("]", "").split(",")  # reform the temperature list
        temperature_list_num = []
        # convert the data into float
        for item in temperature_list_str:
            temperature_list_num.append(float(item))
        temperature_array = np.array(temperature_list_num).reshape(
            (24, 32))  # convert the temperature list into a 24x32 array
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


t_array = []
while True:
    t1 = time.monotonic()  # for determining frame rate
    try:
        data = data_access()
        if data.size > 0:
            update_plot(data)
        else:
            continue
    except:
        continue
    t_array.append(time.monotonic() - t1)
    if len(t_array) > 10:
        t_array = t_array[1:]  # recent times for frame rate approx
    print('Frame Rate: {0:2.1f}fps'.format(len(t_array) / np.sum(t_array)))
