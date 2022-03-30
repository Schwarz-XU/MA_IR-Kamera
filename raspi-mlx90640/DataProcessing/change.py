# change.py
from DataProcessing.filetime_to_unixtime import filetime_to_dt
import pandas as pd

dt = pd.read_csv("../Data/SurfTemp_1150_22-35.csv", delimiter=';')
filetime = dt['Filetime'][len(dt['Filetime'])-1]
print(filetime)

date = filetime_to_dt(filetime).strftime("%Y-%m-%d")
time = filetime_to_dt(filetime).strftime("%H:%M:%S")
print(date)
print(time)
