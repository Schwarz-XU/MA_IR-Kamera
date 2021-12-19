# sub.py
import paho.mqtt.client as mqtt
import csv
import os
from datetime import date, time


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("raspberry/temperature_array")  # sub the topic


def on_message(client, userdata, msg):
    # print(f"{msg.topic} {msg.payload}")
    # write the temperature data into a .csv file
    file_path = os.path.abspath(".")
    print(msg.payload)
    with open(file_path + "/Temperature_Data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(msg.payload)


# establish connection
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.will_set('raspberry/status', b'{"status": "sub_off"}')  # set will to find out if the program is running
client.connect('broker.emqx.io', 1883, 60)


client.loop_forever()
