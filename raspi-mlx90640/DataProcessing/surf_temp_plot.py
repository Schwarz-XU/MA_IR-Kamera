import time
import pandas as pd
import numpy as np
from DataProcessing.filetime_to_unixtime import filetime_to_dt
import matplotlib.pyplot as plt
import seaborn
from pylab import mpl

start = time.perf_counter()
# set the overall front
mpl.rcParams['font.sans-serif'] = ['Times New Roman']
mpl.rcParams['axes.labelsize'] = 14
mpl.rcParams['axes.titlesize'] = 14
# initial params.
headers = ['Filetime', 'Oberflächentemperatur (Soll)', 'Oberflächentemperatur (Ist)', 'VL-Temperatur (Soll)',
           'VL-Temperatur (Ist)', 'RL-Temperatur (Ist)', 'Öffnung des Durchgangsventils (Soll)']
color_list = ['grey', 'lightgreen', 'darkgreen', 'orange', 'red', 'blue', 'black']
band_width = 1
# open the csv files
row_num = 100  # sample time 10 ms, plot data gap 100 * 10 = 1 s
file_2040 = pd.read_csv(f"../Data/SurfTemp_1150_20-40.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_2235 = pd.read_csv(f"../Data/SurfTemp_1150_22-35.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_2835 = pd.read_csv(f"../Data/SurfTemp_1150_28-35.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_3022 = pd.read_csv(f"../Data/SurfTemp_1150_30-22.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_3235 = pd.read_csv(f"../Data/SurfTemp_1150_32-35.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_3520 = pd.read_csv(f"../Data/SurfTemp_1150_35-20.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_3522 = pd.read_csv(f"../Data/SurfTemp_1150_35-22.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_4020 = pd.read_csv(f"../Data/SurfTemp_1150_40-20.csv", delimiter=';',
                        skiprows=lambda x: x > 1 and x % row_num != 0)
file_dict = {"file_2040": file_2040, "file_2235": file_2235, "file_2835": file_2835, "file_3022": file_3022,
             "file_3235": file_3235, "file_3520": file_3520, "file_3522": file_3522, "file_4020": file_4020}


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
                     alpha=0.4, color="yellowgreen", label='Toleranzbereich der Oberflächentemperatur')
    plt.xlabel('Zeit in s', size=14)

    for j in range(1, len(headers)):
        if j != 6:
            file[headers[j]].plot(ax=ax1, style='-', grid=True, alpha=1.0, label=f'{headers[j]}', color=color_list[j])
            ax1.set_yticks(np.arange(10, 65, 5))
            ax1.tick_params(labelsize=14)
            ax1.set_ylabel('Temperatur in °C', size=14)
        else:
            ax2 = ax1.twinx()
            file[headers[j]].plot(ax=ax2, style='--', alpha=0.6, label=f'{headers[j]}', color=color_list[j])
            ax2.tick_params(labelsize=14)
            ax2.set_yticks(np.arange(0, 110, 10))
            ax2.set_ylabel('Öffnung des Durchgangsventils in %', size=14)
    fig.legend(fontsize=14, bbox_to_anchor=(1, 1), bbox_transform=ax1.transAxes)
    ax1.margins(x=0)
    ax2.margins(x=0, y=0)
    plt.suptitle(f'Sprungantwort der Oberflächentemperaturregelung: {temp_start} °C - {temp_end} °C', size=14)
    plt.title(f"{filetime_to_dt(file['Filetime'][0]).strftime('%d.%m.%Y %H:%M:%S')} - "
              f"{filetime_to_dt(file['Filetime'][len(file['Filetime']) - 1]).strftime('%d.%m.%Y %H:%M:%S')}",
              y=1, size=14)

    plt.savefig(f'../Bild/Sprungantwort_Oberflächentemperaturregelung_{temp_start}°C-{temp_end}°C.png',
                dpi=400, bbox_inches='tight')
    # plt.show()
    # break
end = time.perf_counter()
print(end - start)
