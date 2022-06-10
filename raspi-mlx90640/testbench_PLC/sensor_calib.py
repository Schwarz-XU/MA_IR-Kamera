# sensor_calib.py
import paho.mqtt.client as mqtt
import csv
from datetime import datetime
import numpy as np
import time
from queue import Queue

broker_address = "broker.emqx.io"
broker_port = 1883
pt1 = Queue()
pt2 = Queue()
sensor_1215 = Queue()
sensor_1216 = Queue()
sensor_1315 = Queue()
sensor_1316 = Queue()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    client.subscribe("Rkl/WtrSup/zone11/test/pt1")
    client.subscribe("Rkl/WtrSup/zone11/test/pt2")
    client.subscribe("Rkl/raspberry/temperature_array")


def on_message(client, userdata, msg):
    payload = msg.payload
    topic = str(msg.topic)
    if payload != bytes():
        if topic == "Rkl/WtrSup/zone11/test/pt1":
            pt1.put(float(payload))
        elif topic == "Rkl/WtrSup/zone11/test/pt2":
            pt2.put(float(payload))
        elif topic == "Rkl/raspberry/temperature_array":
            temperature_list_str = str(payload.decode("utf-8")).replace("\n", "").replace(" ", "").replace("[","").replace("]", "").split(",")
            temperature_list_num = []
            for item in temperature_list_str:
                temperature_list_num.append(float(item))
            temperature_array = np.array(temperature_list_num).reshape((24, 32))
            sensor_1215.put(temperature_array[12][15])
            sensor_1216.put(temperature_array[12][16])
            sensor_1315.put(temperature_array[13][15])
            sensor_1316.put(temperature_array[13][16])

        else:
            print("No topic matches")
        now = datetime.now()  # get current date and time
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        with open("sensor_calib_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            print([current_date, current_time, pt1.get(), pt2.get(), sensor_1215.get(), sensor_1216.get(), sensor_1315.get(), sensor_1316.get()])
            writer.writerows([current_date, current_time, pt1.get(), pt2.get(), sensor_1216.get(), sensor_1315.get(), sensor_1316.get()])


def run():
    try:
        client = mqtt.Client(clean_session=True)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(broker_address, broker_port)
        client.loop_start()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        run()
