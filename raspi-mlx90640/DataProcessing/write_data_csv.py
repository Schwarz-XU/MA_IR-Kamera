# write_data_csv.py
from DataAcquisition import sub
from datetime import datetime, time
import numpy as np
import time
import csv
import os


def write_csv():
    # receive data from sub.py
    sub.run()
    temperature_array = sub.temperature_array
    temperature_list = sub.temperature_list_str
    # write the temperature data into a .csv file
    file_path = os.path.abspath("../Data")
    with open(file_path + "/temperature_data.csv", "a", newline="") as file:
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
                position_list.append("pos_{i}_{j}".format(i=i, j=j))
        # set headers
        headers = ["Date", "Time"] + position_list
        write_data = [current_date] + [current_time] + temperature_list

        # # write csv file with pandas-library
        # temperature_data = pd.DataFrame([write_data], columns=headers)
        # temperature_data.to_csv(file)

        # write csv file with csv-library
        file_is_empty = os.stat(file_path + "/Temperature_Data.csv").st_size == 0
        if file_is_empty:
            writer.writerow(headers)  # if the file is empty, then write the headers
        writer.writerows([write_data])
    time.sleep(1)  # write data every 1 sec.


def read_csv():
    file_path = os.path.abspath("../Data")
    with open(file_path + "/Temperature_Data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def run():
    write_csv()
    # read_csv()


if __name__ == '__main__':
    while True:
        run()
