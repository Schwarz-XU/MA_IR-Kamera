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
            now = str(datetime.now().strftime("%m%d_%H%M"))
            file_name = now + "__surf_temp_1150.csv"
            with open(file_name, "a", newline="") as file:
                if not temperature_array.size == 0:
                    i += 1
                    temp_79 = temperature_array[7][9]
                    temp_712 = temperature_array[7][12]
                    temp_715 = temperature_array[7][15]
                    temp_718 = temperature_array[7][18]
                    temp_7_arv = np.average([temp_79, temp_712, temp_715, temp_718])
                    temp_99 = temperature_array[9][9]
                    temp_912 = temperature_array[9][12]
                    temp_915 = temperature_array[9][15]
                    temp_918 = temperature_array[9][18]
                    temp_9_arv = np.average([temp_99, temp_912, temp_915, temp_918])
                    temp_119 = temperature_array[11][9]
                    temp_1112 = temperature_array[11][12]
                    temp_1115 = temperature_array[11][15]
                    temp_1118 = temperature_array[11][18]
                    temp_11_arv = np.average([temp_119, temp_1112, temp_1115, temp_1118])
                    temp_1150_arv = np.average([temp_7_arv, temp_9_arv, temp_11_arv])
                    data_list = [i, temp_79, temp_712, temp_715, temp_718, temp_99, temp_912, temp_915,
                                 temp_918, temp_119, temp_1112, temp_1115, temp_1118, temp_7_arv, temp_9_arv,
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
