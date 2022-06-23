from DataAcquisition import sub
from DataProcessing.mov_avg import value_moving_avg
from datetime import datetime
import numpy as np
import csv
import time


class Write_to_csv:

    def __init__(self, file_name, stop_time_in_s):
        self.file_name = file_name
        self.stop_time_in_s = stop_time_in_s

    def start_script(self):
        i = 0
        now1 = datetime.now()
        while True:
            try:
                sub.run()
                pt1 = sub.pt1  # Air temperature
                pt2 = sub.pt2  # Air temperature near the sensor
                pt3 = sub.pt3  # Wall PT100 right
                pt4 = sub.pt4  # Wall PT100 mid
                pt5 = sub.pt5  # Wall PT100 left
                t_sensor = sub.t_sensor  # temperature of sensor according to the manufacture
                Tvl8 = sub.Tvl8  # 1150 VL
                temperature_array = sub.temperature_array
                with open(self.file_name, "a", newline="") as file:
                    if not temperature_array.size == 0:
                        # Band
                        temp_1217 = temperature_array[12][17]
                        temp_1216 = temperature_array[12][16]
                        temp_1117 = temperature_array[11][17]
                        temp_1116 = temperature_array[11][16]
                        temp_avg = np.average([temp_1117, temp_1116, temp_1217, temp_1216])
                        band_temp_mov_avg = value_moving_avg(temp_avg, 10, 0.4).calculate()

                        print(band_temp_mov_avg)
                        print("___________")
                        # Wand
                        temp_613 = temperature_array[6][13]
                        temp_614 = temperature_array[6][14]
                        temp_avg_2 = np.average([temp_613, temp_614])
                        wand_temp_mov_avg = value_moving_avg(temp_avg_2, 10, 0.4).calculate()
                        print(wand_temp_mov_avg)

                        data_list = [i, temp_1217, temp_1216, temp_1117, temp_1116, band_temp_mov_avg,
                                     temp_613, temp_614, wand_temp_mov_avg,
                                     pt1, pt2, pt3, pt4, pt5, t_sensor, Tvl8]
                        i += 1
                        print(data_list)
                        writer = csv.writer(file)
                        writer.writerow(data_list)
                    time.sleep(0.2)
                    if i == self.stop_time_in_s:
                        now2 = datetime.now()
                        time_gap = now2 - now1
                        print(f"finish after {time_gap/60} min")
                        break
                    else:
                        continue
            except Exception as e:
                print(repr(e))
                break
