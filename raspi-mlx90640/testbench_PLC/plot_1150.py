import matplotlib.pyplot as plt
import csv
from datetime import datetime

timestamp = []
temp_79 = []
temp_712 = []
temp_715 = []
temp_718 = []
temp_7_arv = []
temp_99 = []
temp_912 = []
temp_915 = []
temp_918 = []
temp_9_arv = []
temp_119 = []
temp_1112 = []
temp_1115 = []
temp_1118 = []
temp_11_arv = []
temp_1150_arv = []

now = str(datetime.now().strftime("%m%d_%H%M"))
file_name = "0223_1635_surf_temp_1150.csv"
with open(file_name, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        timestamp.append(str(row[0]))
        temp_79.append(float(row[1]))
        temp_712.append(float(row[2]))
        temp_715.append(float(row[3]))
        temp_718.append(float(row[4]))

        temp_99.append(float(row[5]))
        temp_912.append(float(row[6]))
        temp_915.append(float(row[7]))
        temp_918.append(float(row[8]))

        temp_119.append(float(row[9]))
        temp_1112.append(float(row[10]))
        temp_1115.append(float(row[11]))
        temp_1118.append(float(row[12]))

        temp_7_arv.append(float(row[13]))
        temp_9_arv.append(float(row[14]))
        temp_11_arv.append(float(row[15]))
        temp_1150_arv.append(float(row[16]))


plt.subplot(3, 1, 1)
plt.plot(timestamp, temp_79, label='temp_79')
plt.plot(timestamp, temp_712, label='temp_712')
plt.plot(timestamp, temp_715, label='temp_715')
plt.plot(timestamp, temp_718, label='temp_718')
plt.plot(timestamp, temp_7_arv, label='temp_7_arv')
plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.ylabel('temperature')
plt.ylim((25, 40))
plt.title('1150_7xx', loc="right")

plt.subplot(3, 1, 2)
plt.plot(timestamp, temp_99, label='temp_99')
plt.plot(timestamp, temp_912, label='temp_912')
plt.plot(timestamp, temp_915, label='temp_915')
plt.plot(timestamp, temp_918, label='temp_918')
plt.plot(timestamp, temp_9_arv, label='temp_9_arv')
plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.ylabel('temperature')
plt.ylim((25, 40))
plt.title('1150_9xx', loc="right")

plt.subplot(3, 1, 3)
plt.plot(timestamp, temp_119, label='temp_119')
plt.plot(timestamp, temp_1112, label='temp_1112')
plt.plot(timestamp, temp_1115, label='temp_1115')
plt.plot(timestamp, temp_1118, label='temp_1118')
plt.plot(timestamp, temp_11_arv, label='temp_11_arv')
plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.xlabel('timestamp')
plt.ylabel('temperature')
plt.title('1150_11xx', loc="right")
plt.ylim((25, 40))

plt.suptitle(now + 'temp_1150')

plt.show()
