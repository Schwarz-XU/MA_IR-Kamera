# sub.py
import paho.mqtt.client as mqtt
import numpy as np

# broker_address = "mqtt.eclipseprojects.io"
broker_address = "broker.emqx.io"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    # print(f"Connected with result code {rc}")
    client.subscribe("raspberry/temperature_array")  # sub the topic


payload = bytes()  # initial the payload var. as a empty bytes var.
temperature_array = np.array([])
temperature_list_str = [""]


def on_message(client, userdata, msg):
    # receive the temperature data from broker
    global payload
    global temperature_array
    global temperature_list_str
    payload = msg.payload
    if payload == bytes():
        print("the data_payload is empty")
        pass
    else:
        temperature_list_str = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").replace("]", "").split(",")  # reform the temperature list
        temperature_list_num = []
        # convert the data into float
        for item in temperature_list_str:
            temperature_list_num.append(float(item))
        temperature_array = np.array(temperature_list_num).reshape(
            (24, 32))  # convert the temperature list into a 24x32 array


def run():
    # establish connection
    client = mqtt.Client(clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.will_set('raspberry/sub/status', b'{"status": "off"}')  # set last will to find out if the program is running
    client.connect(broker_address, broker_port, 60)
    # start the loop
    client.loop_start()
    # client.loop_forever()


if __name__ == '__main__':
    while True:
        run()
