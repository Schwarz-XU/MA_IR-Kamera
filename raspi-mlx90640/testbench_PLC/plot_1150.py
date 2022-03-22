import matplotlib.pyplot as plt
import csv
from datetime import datetime

timestamp = []
temp_715 = []
temp_718 = []
temp_721 = []
temp_724 = []
temp_7_arv = []
temp_915 = []
temp_918 = []
temp_921 = []
temp_924 = []
temp_9_arv = []
temp_1115 = []
temp_1118 = []
temp_1121 = []
temp_1124 = []
temp_11_arv = []
temp_1150_arv = []

now = str(datetime.now().strftime("%m%d_%H%M"))
file_name = "../Data/0321_1216_surf_temp_1150.csv"
with open(file_name, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        timestamp.append(str(row[0]))
        temp_715.append(float(row[1]))
        temp_718.append(float(row[2]))
        temp_721.append(float(row[3]))
        temp_724.append(float(row[4]))

        temp_915.append(float(row[5]))
        temp_918.append(float(row[6]))
        temp_921.append(float(row[7]))
        temp_924.append(float(row[8]))

        temp_1115.append(float(row[9]))
        temp_1118.append(float(row[10]))
        temp_1121.append(float(row[11]))
        temp_1124.append(float(row[12]))

        temp_7_arv.append(float(row[13]))
        temp_9_arv.append(float(row[14]))
        temp_11_arv.append(float(row[15]))
        temp_1150_arv.append(float(row[16]))


plt.subplot(4, 1, 1)
plt.plot(timestamp, temp_715, label='temp_715')
plt.plot(timestamp, temp_718, label='temp_718')
plt.plot(timestamp, temp_721, label='temp_721')
plt.plot(timestamp, temp_724, label='temp_724')
plt.plot(timestamp, temp_7_arv, label='temp_7_arv')
# plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.ylabel('temperature')
plt.ylim((20, 30))
plt.title('1150_7xx', loc="right")

plt.subplot(4, 1, 2)
plt.plot(timestamp, temp_915, label='temp_915')
plt.plot(timestamp, temp_918, label='temp_918')
plt.plot(timestamp, temp_921, label='temp_921')
plt.plot(timestamp, temp_924, label='temp_924')
plt.plot(timestamp, temp_9_arv, label='temp_9_arv')
# plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.ylabel('temperature')
plt.ylim((20, 30))
plt.title('1150_9xx', loc="right")

plt.subplot(4, 1, 3)
plt.plot(timestamp, temp_1115, label='temp_1115')
plt.plot(timestamp, temp_1118, label='temp_1118')
plt.plot(timestamp, temp_1121, label='temp_1121')
plt.plot(timestamp, temp_1124, label='temp_1124')
plt.plot(timestamp, temp_11_arv, label='temp_11_arv')
# plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.xlabel('timestamp')
plt.ylabel('temperature')
plt.title('1150_11xx', loc="right")
plt.ylim((20, 30))


plt.subplot(4, 1, 4)
plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.ylabel('temperature')
plt.ylim((20, 30))
plt.title('1150_arv', loc="right")

plt.suptitle(now + 'temp_1150')

plt.show()
