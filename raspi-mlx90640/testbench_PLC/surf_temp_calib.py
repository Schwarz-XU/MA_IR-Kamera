from DataAcquisition import sub
import csv
from datetime import datetime
import time
import numpy as np

i = 0
now = str(datetime.now().strftime("%m%d_%H%M"))
file_name = now + "_surf_temp_1150.csv"

if __name__ == '__main__':
    while True:
        try:
            sub.run()
            temperature_array = sub.temperature_array

            with open(file_name, "a", newline="") as file:
                if not temperature_array.size == 0:
                    temp_715 = temperature_array[7][15]
                    temp_718 = temperature_array[7][18]
                    temp_721 = temperature_array[7][21]
                    temp_724 = temperature_array[7][24]
                    temp_7_arv = np.average([temp_715, temp_718, temp_721, temp_724])
                    temp_915 = temperature_array[9][15]
                    temp_918 = temperature_array[9][18]
                    temp_921 = temperature_array[9][21]
                    temp_924 = temperature_array[9][24]
                    temp_9_arv = np.average([temp_915, temp_918, temp_921, temp_924])
                    temp_1115 = temperature_array[11][15]
                    temp_1118 = temperature_array[11][18]
                    temp_1121 = temperature_array[11][21]
                    temp_1124 = temperature_array[11][24]
                    temp_11_arv = np.average([temp_1115, temp_1118, temp_1121, temp_1124])
                    temp_1150_arv = np.average([temp_7_arv, temp_9_arv, temp_11_arv])
                    data_list = [i, temp_715, temp_718, temp_721, temp_724, temp_915, temp_918, temp_921,
                                 temp_924, temp_1115, temp_1118, temp_1121, temp_1124, temp_7_arv, temp_9_arv,
                                 temp_11_arv, temp_1150_arv]
                    i += 1
                    print(data_list)
                    writer = csv.writer(file)
                    writer.writerow(data_list)
                time.sleep(1)
                if i == 600:
                    print("finish after 10min")
                    break
                else:
                    continue
        except Exception as e:
            print(repr(e))
            break
