# sub.py
import paho.mqtt.client as mqtt
import numpy as np

# broker_address = "mqtt.eclipseprojects.io"
# broker_address = "broker.emqx.io"
broker_address = "broker.hivemq.com"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    # print(f"Connected with result code {rc}")
    topic = [("Rkl/raspberry/temperature_array", 2), ("Rkl/WtrSup/zone11/test/pt1", 0), ("Rkl/WtrSup/zone11/test/pt2", 0),
             ("Rkl/WtrSup/zone11/test/pt3", 0), ("Rkl/WtrSup/zone11/test/pt4", 0), ("Rkl/WtrSup/zone11/test/pt5", 0),
             ("Rkl/WtrSup/zone11/Tvl8", 0)]
             #("Rkl/WtrSup/zone11/PanelData")]

    client.subscribe(topic)

payload = bytes()  # initial the payload var. as an empty byte var.
temperature_array = np.array([])
temperature_list_str = [""]
pt1, pt2, pt3, pt4, pt5, Tvl8 = float(), float(), float(), float(), float(), float()


def on_message(client, userdata, msg):
    # receive the temperature data from broker
    global payload
    global temperature_array
    global temperature_list_str
    global pt1, pt2, pt3, pt4, pt5, Tvl8
    #global panel_data

    payload = msg.payload
    topic = msg.topic

    if payload == bytes():
        print("the data_payload is empty")
        pass
    else:
        if topic == "Rkl/raspberry/temperature_array":
            temperature_list_str = str(payload, encoding="utf-8").replace("\n", "").replace(" ", "").replace("[", "").\
                replace("]", "").split(",")  # reform the temperature list
            temperature_list_num = []
            # convert the data into float
            for item in temperature_list_str:
                temperature_list_num.append(float(item))
            temperature_array = np.array(temperature_list_num).reshape((24, 32))  # convert the temperature list into a 24x32 array
        if topic == "Rkl/WtrSup/zone11/test/pt1":
            pt1 = float(payload)
        if topic == "Rkl/WtrSup/zone11/test/pt2":
            pt2 = float(payload)
        if topic == "Rkl/WtrSup/zone11/test/pt3":
            pt3 = float(payload)
        if topic == "Rkl/WtrSup/zone11/test/pt4":
            pt4 = float(payload)
        if topic == "Rkl/WtrSup/zone11/test/pt5":
            pt5 = float(payload)
        if topic == "Rkl/WtrSup/zone11/Tvl8":
            Tvl8 = float(payload)
        # if topic == "RKl/WtrSup/zone11/PanelData":
        #     panel_data = payload
        #     print(payload)


def run():
    # establish connection
    client = mqtt.Client(clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.will_set('Rkl/raspberry/sub/status', b'{"status": "off"}')  # set last will to find out if the program is running
    client.connect(broker_address, broker_port, 60)
    # start the loop
    client.loop_start()
    # client.loop_forever()


if __name__ == '__main__':
    while True:
        run()
