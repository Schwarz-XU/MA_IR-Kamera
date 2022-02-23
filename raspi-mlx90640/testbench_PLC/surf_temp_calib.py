from DataAcquisition import sub
import csv
from datetime import datetime
import time
import numpy as np
import paho.mqtt.client as mqtt

i = 0
if __name__ == '__main__':
    while True:
        try:
            sub.run()
            temperature_array = sub.temperature_array
            with open("surf_temp_1150.csv", "a", newline="") as file:
                if not temperature_array.size == 0:
                    i += 1
                    temp_710 = temperature_array[7][10]
                    temp_714 = temperature_array[7][14]
                    temp_718 = temperature_array[7][18]
                    temp_722 = temperature_array[7][22]
                    temp_7_arv = np.average([temp_710, temp_714, temp_718, temp_722])
                    temp_910 = temperature_array[9][10]
                    temp_914 = temperature_array[9][14]
                    temp_918 = temperature_array[9][18]
                    temp_922 = temperature_array[9][22]
                    temp_9_arv = np.average([temp_910, temp_914, temp_918, temp_922])
                    temp_1110 = temperature_array[11][10]
                    temp_1114 = temperature_array[11][14]
                    temp_1118 = temperature_array[11][18]
                    temp_1122 = temperature_array[11][22]
                    temp_11_arv = np.average([temp_1110, temp_1114, temp_1118, temp_1122])
                    temp_1150_arv = np.average([temp_7_arv, temp_9_arv, temp_11_arv])
                    data_list = [i, temp_710, temp_714, temp_718, temp_722, temp_910, temp_914, temp_918,
                                 temp_922, temp_1110, temp_1114, temp_1118, temp_1122, temp_7_arv, temp_9_arv,
                                 temp_11_arv, temp_1150_arv]
                    print(data_list)
                    writer = csv.writer(file)
                    writer.writerow(data_list)
                time.sleep(1)
                if i == 600:
                    break
                else:
                    continue
        except Exception as e:
            print(repr(e))
            break
