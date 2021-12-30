# write_data.py
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
    if payload == bytes():
        pass  # if payload is empty, then pass
    else:
        temperature_list = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace("]", "").split(",")  # reform the temperature list
        temperature_array = np.array(temperature_list).reshape((24, 32))  # convert the temperature list into a 24x32 array
        # write the temperature data into a .csv file
        file_path = os.path.abspath("../Data")
        with open(file_path + "/Temperature_Data.csv", "a", newline="") as file:
            # writer = csv.writer(file, delimiter=',', quotechar='"')
            writer = csv.writer(file)
            # get current date and time
            now = datetime.now()  # get current date and time
            current_date = now.strftime("%Y-%m-%d")
            current_time = now.strftime("%H:%M:%S")
            # initial positions of the pixels, add them to headers
            position_list = []
            for i in range(0, np.shape(temperature_array)[0]):
                for j in range(0, np.shape(temperature_array)[1]):
                    position_list.append(str((i, j)))
            # set headers
            headers = ["Date", "Time"] + position_list
            write_data = [current_date] + [current_time] + temperature_list
            # print(headers)
            # print([write_data])

            # # write csv file with pandas-package
            # temperature_data = pd.DataFrame([write_data], columns=headers)
            # temperature_data.to_csv(file)

            # write csv file with csv-package
            file_is_empty = os.stat(file_path + "/Temperature_Data.csv").st_size == 0
            if file_is_empty:
                writer.writerow(headers)  # if the file is empty, then write the headers
            writer.writerows([write_data])
            # TODO: categorize the data with date.
        time.sleep(2)


def read_csv():
    file_path = os.path.abspath("../Data")
    with open(file_path + "/Temperature_Data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def update_plot():
    print(temperature_array)


def run_write():
    write_csv()
    # read_csv()
