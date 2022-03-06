import pandas as pd
import numpy as np
import time
import csv

surf_temp_list = ["20-40", "22-35", "28-35", "30-22", "32-35", "35-20", "35-22", "40-20"]
file_path = f"../Data/SurfTemp_1150_{surf_temp_list[0]}.csv"

with open(file_path, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
