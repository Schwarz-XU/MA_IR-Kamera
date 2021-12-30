# from datetime import datetime
#
# name_list = []
# for i in range(0, 24):
#     for j in range(0, 32):
#         name_list.append(str((i, j)))
# print(name_list)
# headers = ["Date", "Time"] + name_list
# print(headers)
# # now = datetime.now()
# #
# # current_date = now.strftime("%Y.%m.%d")
# # current_time1 = now.strftime("%H:%m:%s")
# # current_time2 = now.strftime("%H:%M:%S")
# # print(current_date)
# # print(current_time1)
# # print(current_time2)

import csv

headers = ["class", "name", "sex"]

rows = [
    [1, "xiaoming", "male"],
    [1, "xiaoming2", "female"],
    [2, "xiaoming3", "male"],
    [2, "xiaoming4", "female"],
]

with open ("test.csv", "w") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
