import matplotlib.pyplot as plt
import csv
from datetime import datetime
from more_itertools import chunked
import pandas as pd

timestamp = []
sup_temp = []
surf_temp = []
time = []
time_gap = 10

now = str(datetime.now().strftime("%m%d_%H%M"))
file_name = "resp_surf-sup.csv"
with open(file_name, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        timestamp.append(str(row[0]))
        sup_temp.append(float(row[1]))
        surf_temp.append(float(row[2]))

    for i in range(0, int(len(timestamp)/time_gap)):
        time.append(i)

    sup_temp_arv = [sum(x) / len(x) for x in chunked(sup_temp, time_gap)]
    surf_temp_arv = [sum(x) / len(x) for x in chunked(surf_temp, time_gap)]

dict = {"sup_temp_arv": sup_temp_arv, "surf_temp_arv": surf_temp_arv}
df = pd.DataFrame(dict)
df.to_csv("surf_sup_arv.csv")

plt.subplot(1, 1, 1)
plt.plot(time, sup_temp_arv, label='sup_temp_arv')
plt.plot(time, surf_temp_arv, label='surf_temp_arv')
x_major_locator = plt.MultipleLocator(50)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.legend(loc='upper right')
plt.ylabel('temperature')
#plt.ylim((34, 38))
plt.title('1150_temp', loc="right")
plt.suptitle(file_name)

plt.show()