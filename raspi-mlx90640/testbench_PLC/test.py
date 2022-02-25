# test.py
import time

from DataAcquisition import sub
import numpy as np


sub.run()
while 1:
    if sub.temperature_array.size != 0:
        print(sub.temperature_array[0][0])
        print(sub.temperature_array[0][31])
        print(sub.temperature_array[23][0])
        print(sub.temperature_array[23][31])
        time.sleep(1)
