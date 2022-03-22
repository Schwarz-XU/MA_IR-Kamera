# sup_temp_plot.py
import time
import pandas as pd
import numpy as np
from DataProcessing.filetime_to_unixtime import filetime_to_dt
import matplotlib.pyplot as plt
import seaborn
from pylab import mpl

start = time.perf_counter()
# set the overall front
mpl.rcParams['font.sans-serif'] = ['Arial']
mpl.rcParams['axes.labelsize'] = 14
mpl.rcParams['axes.titlesize'] = 14
# initial params.
headers = ['Filetime', 'VL-Temperatur (Soll)', 'VL-Temperatur (Ist)', 'RL-Temperatur (Ist)',
           'Öffnung des Durchgangsventils (Soll)']
color_list = ['grey', 'orange', 'red', 'blue', 'black']
band_width = 1
# open the csv files
row_num = 100  # sample time 10 ms, plot data gap 100 * 10 = 1 s
file_1545 = pd.read_csv(f"../Data/SupTemp_1150_15-45.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_2540 = pd.read_csv(f"../Data/SupTemp_1150_25-40.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_3035 = pd.read_csv(f"../Data/SupTemp_1150_30-35.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_3540 = pd.read_csv(f"../Data/SupTemp_1150_35-40.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_2_3540 = pd.read_csv(f"../Data/SupTemp_1150_35-40_2.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_4015 = pd.read_csv(f"../Data/SupTemp_1150_40-15.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_4035 = pd.read_csv(f"../Data/SupTemp_1150_40-35.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_404540 = pd.read_csv(f"../Data/SupTemp_1150_40-45-40.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_4515 = pd.read_csv(f"../Data/SupTemp_1150_45-15.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_4530 = pd.read_csv(f"../Data/SupTemp_1150_45-30.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
# file_dict = {"file_2_3540": file_2_3540}

file_dict = {"file_1545": file_1545, "file_2540": file_2540, "file_3035": file_3035, "file_3540": file_3540,
             "file_2_3540": file_2_3540, "file_4015": file_4015, "file_4035": file_4035, "file_404540": file_404540,
             "file_4515": file_4515, "file_4530": file_4530}

for name, file in file_dict.items():
    # headers = list(file.columns.values[1:7])
    # headers[1:2] = headers[2:1]
    print(headers)
    print(name)
    print(file)
    # add marker
    file_dict[name]['Marke'] = int(name[-2:])
    temp_start = name[-4:-2]
    temp_end = name[-2:]
    print(temp_start, temp_end)
    # filetime to unix time
    for item in file['Filetime']:
        file['Datum'] = filetime_to_dt(item).strftime('%Y-%m-%d')
        file['Zeit'] = filetime_to_dt(item).strftime('%H:%M:%S')
    # plot
    fig = plt.figure(figsize=(16, 9))
    ax1 = fig.add_subplot(111)
    plt.fill_between(file.index, file['Marke'] + band_width, file['Marke'] - band_width,
                     alpha=0.4, color="yellowgreen", label='Toleranzbereich der VL-Temperatur')
    plt.xlabel('Zeit in s' + '\n' + f"{filetime_to_dt(file['Filetime'][0]).strftime('%d.%m.%Y %H:%M:%S')} - "
               f"{filetime_to_dt(file['Filetime'][len(file['Filetime']) - 1]).strftime('%d.%m.%Y %H:%M:%S')}", size=14)

    for j in range(1, len(headers)):
        if j == 2:
            file[headers[j]].plot(ax=ax1, style='-', alpha=1.0, label=f'{headers[j]}', color=color_list[j], linewidth=3)
        elif j != 4:
            file[headers[j]].plot(ax=ax1, style='-', grid=True , alpha=1.0, label=f'{headers[j]}', color=color_list[j])
            ax1.set_yticks(np.arange(10, 65, 5))
            ax1.tick_params(labelsize=14)
            ax1.set_ylabel('Temperatur in °C', size=14)
            # ax1.spines['left'].set_color(color_list[0])
            # ax1.spines['right'].set_color(color_list[0])
            # ax1.spines['bottom'].set_color(color_list[0])
            # ax1.spines['top'].set_color(color_list[0])
        else:
            ax2 = ax1.twinx()
            file[headers[j]].plot(ax=ax2, style='--', alpha=0.6, label=f'{headers[j]}', color=color_list[j])
            ax2.tick_params(labelsize=14)
            ax2.set_yticks(np.arange(0, 110, 10))
            ax2.set_ylabel('Öffnung des Durchgangsventils in %', size=14)
            # ax2.spines['left'].set_color(color_list[0])
            # ax2.spines['right'].set_color(color_list[0])
            # ax2.spines['bottom'].set_color(color_list[0])
            # ax2.spines['top'].set_color(color_list[0])
    fig.legend(fontsize=14, bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)
    ax1.margins(x=0)
    if int(temp_end) - int(temp_start) > 25:
        ax2.margins(x=0, y=0)
    plt.title(f'Sprungantwort der VL-Temperaturregelung: {temp_start} °C - {temp_end} °C', size=16)
    # plt.title(f"{filetime_to_dt(file['Filetime'][0]).strftime('%d.%m.%Y %H:%M:%S')} - "
    #           f"{filetime_to_dt(file['Filetime'][len(file['Filetime']) - 1]).strftime('%d.%m.%Y %H:%M:%S')}",
    #           y=1, size=14)

    plt.savefig(f'../Bergfest/Sprungantwort der VL-Temperaturregelung_{temp_start}°C-{temp_end}°C.png',
                dpi=400, bbox_inches='tight')
    # plt.show()
    # break
end = time.perf_counter()
print(end - start)
