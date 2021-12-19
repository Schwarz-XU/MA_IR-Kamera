# sub.py
import paho.mqtt.client as mqtt
import csv
import os
# from datetime import date, time
import time


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("raspberry/temperature_array")  # sub the topic


def on_message(client, userdata, msg):
    # print(f"{msg.topic} {msg.payload}")
    # print(msg.payload)
    temperature_array = str(msg.payload, encoding="utf-8")\
        .replace("\n", "").replace(" ", "").replace("[", "").replace("]", "")\
        .split(",")
    print(temperature_array)
    # write the temperature data into a .csv file
    file_path = os.path.abspath(".")
    with open(file_path + "/Temperature_Data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        for i in temperature_array:
            writer.writerow(i)


# establish connection
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.will_set('raspberry/status', b'{"status": "sub_off"}')  # set will to find out if the program is running
client.connect('broker.emqx.io', 1883, 60)

client.loop_forever()
