# update_plot.py
from TemperatureMeasurement import sub
from datetime import datetime, date, time
import numpy as np
import pandas as pd
import queue
import time
import sys
import csv
import os


# initial the global var.
payload = bytes()
temperature_list = []
temperature_array = np.array("")


def write_csv():
    # receive data from sub.py
    sub.run_sub()
    global payload
    global temperature_list
    global temperature_array
    payload = sub.payload
    payload = sub.payload
    if payload == bytes():
        pass  # if payload is empty, then pass
    else:
        temperature_list = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace(
            "]", "").split(",")  # reform the temperature list
        temperature_array = np.array(temperature_list).reshape(
            (24, 32))  # convert the temperature list into a 24x32 array
