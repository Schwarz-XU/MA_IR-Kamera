# write_data.py
from TemperatureMeasurement import sub
from datetime import datetime
import numpy as np
import pandas as pd
import time
import sys
import queue
import csv
import os

# receive data from sub.py
while True:
    sub.run_sub()
    payload = sub.payload
    if payload == bytes():
        pass
    else:
        temperature_list = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace("]", "").split(",")  # reform the temperature list
        print(temperature_list)

    # write the temperature data into a .csv file
    file_path = os.path.abspath(".")
    with open(file_path + "/Temperature_Data.csv", "a", newline="") as file:
        writer = csv.writer(file, delimiter=' ', quotechar=' ')
        now = datetime.now().timestamp()  # get current date and time, convert it into timestamp

        headers = ["Date", "Time", "Temperature"]
        sub_headers = [" ", " ", "(0,0)", "(0,1)", "(0,2)", "(0,3)"]  # TODO: automatically set coordinates of pixels
        writer.writerow(headers)
        writer.writerow(sub_headers)
        for temperature in temperature_list:
            writer.writerow(temperature)
    time.sleep(2)
