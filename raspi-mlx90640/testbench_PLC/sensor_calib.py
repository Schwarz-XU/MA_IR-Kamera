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


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    client.subscribe("Rkl/WtrSup/zone11/test/pt1")
    client.subscribe("Rkl/WtrSup/zone11/test/pt2")
    #client.subscribe("raspberry/temperature_array")


def on_message(client, userdata, msg):
    payload = msg.payload
    topic = str(msg.topic)
    if topic == "Rkl/WtrSup/zone11/test/pt1":
        pt1.put(float(payload))
    elif topic == "Rkl/WtrSup/zone11/test/pt2":
        pt2.put(float(payload))
    else:
        print("No topic matches")
    now = datetime.now()  # get current date and time
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    with open("pt_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        print([current_date, current_time, pt1.get(), pt2.get()])
        writer.writerows([current_date, current_time, pt1.get(), pt2.get()])


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
