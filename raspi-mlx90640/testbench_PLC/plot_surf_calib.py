import matplotlib.pyplot as plt
import csv
from datetime import datetime
from more_itertools import chunked

timestamp = []
sensor_temp = []
sup_temp = []
pt_temp = []
time = []
diff = []
time_gap = 10

now = str(datetime.now().strftime("%m%d_%H%M"))
file_name = "../Data/0610_0046_surf_temp_1150_calib.csv"
with open(file_name, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        timestamp.append(str(row[0]))
        sensor_temp.append(float(row[8]))
        pt_temp.append(float(row[-2]))
        sup_temp.append(float(row[-1]))
        diff.append(float(row[8]) - float(row[-2]))
    for i in range(0, int(600/time_gap)):
       time.append(i)

    temp_1150_t10s_arv = [sum(x) / len(x) for x in chunked(sensor_temp, time_gap)]

fig, ax1 = plt.subplots()
ax1.plot(sensor_temp, label='Sensor_Temp')
ax1.plot(sup_temp, label='VL-Temp')
ax1.plot(pt_temp, label='PT1000_Wand_Temp')
ax1.set_ylabel('Temperatur')
ax1.set_ylim(32,35)
ax1.legend(loc='upper right')

ax2 = ax1.twinx()
ax2.set_ylabel('Temperaturdifferenz in K')
ax2.plot(diff, label='Diff_Sensor-PT', color="red")
ax2.set_ylim(0, 1)
ax2.legend(loc='upper left')
#plt.ylim((34, 38))

plt.show()
