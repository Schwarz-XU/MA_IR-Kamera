import matplotlib.pyplot as plt
import csv

timestamp = []
temp_710 = []
temp_714 = []
temp_718 = []
temp_722 = []
temp_7_arv = []
temp_910 = []
temp_914 = []
temp_918 = []
temp_922 = []
temp_9_arv = []
temp_1110 = []
temp_1114 = []
temp_1118 = []
temp_1122 = []
temp_11_arv = []
temp_1150_arv = []

with open('surf_temp_1150.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        timestamp.append(str(row[0]))
        temp_710.append(float(row[1]))
        temp_714.append(float(row[2]))
        temp_718.append(float(row[3]))
        temp_722.append(float(row[4]))

        temp_910.append(float(row[5]))
        temp_914.append(float(row[6]))
        temp_918.append(float(row[7]))
        temp_922.append(float(row[8]))

        temp_1110.append(float(row[9]))
        temp_1114.append(float(row[10]))
        temp_1118.append(float(row[11]))
        temp_1122.append(float(row[12]))

        temp_7_arv.append(float(row[13]))
        temp_9_arv.append(float(row[14]))
        temp_11_arv.append(float(row[15]))
        temp_1150_arv.append(float(row[16]))


plt.subplot(3, 1, 1)
plt.plot(timestamp, temp_710, label='temp_710')
plt.plot(timestamp, temp_714, label='temp_714')
plt.plot(timestamp, temp_718, label='temp_718')
plt.plot(timestamp, temp_722, label='temp_722')
plt.plot(timestamp, temp_7_arv, label='temp_7_arv')
plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(10)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.xlabel('timestamp')
plt.ylabel('temperature')
plt.title('1150_7xx')

plt.subplot(3, 1, 2)
plt.plot(timestamp, temp_910, label='temp_910')
plt.plot(timestamp, temp_914, label='temp_914')
plt.plot(timestamp, temp_918, label='temp_918')
plt.plot(timestamp, temp_922, label='temp_922')
plt.plot(timestamp, temp_9_arv, label='temp_9_arv')
plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(10)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.xlabel('timestamp')
plt.ylabel('temperature')
plt.title('1150_9xx')

plt.subplot(3, 1, 3)
plt.plot(timestamp, temp_1110, label='temp_1110')
plt.plot(timestamp, temp_1114, label='temp_1114')
plt.plot(timestamp, temp_1118, label='temp_1118')
plt.plot(timestamp, temp_1122, label='temp_1122')
plt.plot(timestamp, temp_11_arv, label='temp_11_arv')
plt.plot(timestamp, temp_1150_arv, label='temp_1150_arv')
x_major_locator = plt.MultipleLocator(10)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.xlabel('timestamp')
plt.ylabel('temperature')
plt.title('1150_11xx')
plt.ylim((15, 30))

plt.suptitle('temp_1150')

plt.show()
