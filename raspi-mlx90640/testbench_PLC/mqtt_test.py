import paho.mqtt.client as mqtt
import time
from queue import Queue

import pyads

connected = False
Message_received = False
# payload = bytes()
broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883
plc_address = "5.78.127.222.1.1"
plc_port = 851
q = Queue()


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            global connected
            connected = True
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker_address, broker_port)
    return client


def plc_write(plc, queue, var_address, var_type):
    if not queue.empty():
        print("queue not empty")
        plc.write_by_name(var_address, queue.get(), var_type)
        print(var_address)
        print(var_type)
        print(queue.get())
    else:
        print(f"{queue} is empty")


def subscribe(client: mqtt):
    plc = pyads.Connection(plc_address, plc_port)
    plc.open()

    def on_message(client, userdata, msg):
        topic = str(msg.topic)
        payload = msg.payload.decode("utf-8")
        print(f"Received `{payload}` from `{topic}` topic")
        if topic == "rkl/test/1":
            q.put(str(payload))
        plc_write(plc, queue=q, var_address="gvl_test", var_type=pyads.PLCTYPE_INT)
    client.subscribe("rkl/test/1")
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    while not connected:
        time.sleep(0.1)


if __name__ == '__main__':
    run()
