import time
import mysql.connector
from datetime import datetime
from DataAcquisition import sub

# establish database in localhost

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Sql001601027@',
    database='rkl_temperature'
)
'''
db = mysql.connector.connect(
    host='uelrkl.cvquuhppqhkb.eu-central-1.rds.amazonaws.com',
    user='admin',
    passwd='uelrkl123456',
    database='rkl_ir_temperature'
)
'''

cursor = db.cursor()

position_list = []
q1 = ["INSERT INTO temperature_11xx (data, time, "]
q2 = ["("]
for i in range(0, 24):
    for j in range(0, 32):
        position_list.append("pos_{i}_{j}".format(i=i, j=j))
        q1.append("pos_{i}_{j}".format(i=i, j=j) + ", ")
        q2.append("%s, ")
q3 = "".join(q1).strip(', ') + ')' + ' VALUES '
q4 = "".join(q2) + '%s, %s)'
q5 = q3 + q4  # create the sql-command to insert 770 data


def write_db():
    # prepare_data
    sub.run()
    # payload = sub.payload
    temperature_array = sub.temperature_array
    if temperature_array.size == 0:
    # if payload == bytes():
        print("no data from the sensor, please wait for 2 sec or check the sensor")
        pass  # if payload is empty, then pass
    else:
        # temperature_list = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace("]", "").split(",")  # reform the temperature list
        temperature_list = sub.temperature_list_str
        # get current date and time
        now = datetime.now()  # get current date and time
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        # prepare the data in a tuple
        write_data = ([current_date] + [current_time] + temperature_list)
        cursor.execute("SHOW TABLES")
        if not cursor.fetchall():
            print("initial table")
            cursor.execute("CREATE TABLE temperature_11xx (id smallint PRIMARY KEY AUTO_INCREMENT, data VARCHAR(20) NOT NULL, time VARCHAR(20) NOT NULL)")
            for position in position_list:
                q6 = "ALTER TABLE temperature_11xx ADD COLUMN `{x}` VARCHAR(10) NOT NULL".format(x=position)
                print("insert " + position)
                cursor.execute(q6)
        else:
            pass
        # execute the insert command
        try:
            cursor.execute(q5, write_data)
            time.sleep(5)  # insert data every 5 s
            db.commit()
        except:
            print("Error: please check the execute process")
            print(db.rollback())


def run():
    write_db()


if __name__ == '__main__':
    while True:
        cursor.execute("SHOW TABLES")
        if cursor.fetchall():
            initial_table = input("Do you want to initial the sql-table? (yes/no)")
            if initial_table == "yes":
                cursor.execute("DROP Table temperature_11xx")
            elif initial_table == "no":
                while True:
                    run()
        else:
            while True:
                run()
