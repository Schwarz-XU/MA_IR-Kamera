import pandas as pd

file_path = "../Data/temperature_data.csv"
file = pd.read_csv(file_path, delimiter=',')

print(file['pos_11_17'], file['pos_11_11'], file['pos_11_6'])

# df = file.iloc(file['Time'] > '15:34:30')
df2 = file[['Date', 'Time', 'pos_11_17', 'pos_11_11', 'pos_11_6']]
print(df2.loc(df2['Date'] == '2022-03-07'))

