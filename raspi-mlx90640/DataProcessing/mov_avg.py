import time
import numpy as np
import random


class value_moving_avg:
    def __init__(self, in_val, time_gap, cyc_time, buffer_array=[]):
        self.in_val = in_val
        self.time_gap = time_gap
        self.cyc_time = cyc_time
        self.buffer_array = buffer_array

    def mov_avg(self):
        self.buffer_array.append(self.in_val)
        time.sleep(self.cyc_time)
        if len(self.buffer_array) >= int(self.time_gap / self.cyc_time):
            out_val = np.sum(self.buffer_array[-int(self.time_gap / self.cyc_time):]) / int(self.time_gap / self.cyc_time)
            print(self.buffer_array)
        else:
            out_val = np.sum(self.buffer_array) / (self.time_gap / self.cyc_time)
            print(f"wait for {self.time_gap / self.cyc_time} values")
        return out_val


# while True:
#     input_vals = 100
#     a = value_moving_avg(input_vals, 10, 0.1).mov_avg()
#     print(a)
