import paho.mqtt.client as mqtt
import time
from datetime import datetime
from queue import Queue
import numpy as np
import pyads

connected = False
Message_received = False
#broker_address = "mqtt.eclipseprojects.io"
broker_address = "broker.emqx.io"
broker_port = 1883
plc_address = "5.78.127.222.1.1"
plc_port = 851
P1110_SurfTemp = Queue()
P1120_SurfTemp = Queue()
P1130_SurfTemp = Queue()
P1140_SurfTemp = Queue()
P1150_SurfTemp = Queue()
P1160_SurfTemp = Queue()
P1150_SurfTemp_arv = []
temperature_array = np.array([])


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            global connected
            connected = True
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt.Client(client_id = "Rkl_TwinCAT", clean_session=True)
    client.on_connect = on_connect
    client.connect(broker_address, broker_port)
    return client


def plc_write(plc, queue, var_address, var_type):
    if not queue.empty():
        print("queue not empty")
        plc.write_by_name(var_address, queue.get(), var_type)
    else:
        print(f"{queue} is empty")

class CalMeanVar():
    def __init__(self):
        self.count = 0
        self.A = 0
        self.A_ = 0

    def cal(self, data):
        self.count += 1
        if self.count == 1:
            self.A_ = data
            self.A = data
            return
        self.A_ = self.A
        self.A = self.A + (data - self.A) / self.count


def subscribe(client: mqtt):
    plc = pyads.Connection(plc_address, plc_port)
    plc.open()
    print(plc)
    def on_message(client, userdata, msg):
        global temperature_array
        payload = msg.payload
        topic = msg.topic
        if payload == bytes():
            print("empty payload")
        else:
            temperature_list_str = str(payload.decode("utf-8")).replace("\n", "").replace(" ", "").replace("[", "").replace("]", "").split(",")
            temperature_list_num = []
            for item in temperature_list_str:
                temperature_list_num.append(float(item))
            temperature_array = np.array(temperature_list_num).reshape((24,32))
            print(datetime.now().strftime("%H:%M:%S"))
            #print(f"Received `{payload}` from `{topic}` topic")
            if temperature_array.size != 0:
                temp_715 = temperature_array[7][15]
                temp_718 = temperature_array[7][18]
                temp_721 = temperature_array[7][21]
                temp_724 = temperature_array[7][24]
                temp_7_arv = np.average([temp_715, temp_718, temp_721, temp_724])
                temp_915 = temperature_array[9][15]
                temp_918 = temperature_array[9][18]
                temp_921 = temperature_array[9][21]
                temp_924 = temperature_array[9][24]
                temp_9_arv = np.average([temp_915, temp_918, temp_921, temp_924])
                temp_1115 = temperature_array[11][15]
                temp_1118 = temperature_array[11][18]
                temp_1121 = temperature_array[11][21]
                temp_1124 = temperature_array[11][24]
                temp_11_arv = np.average([temp_1115, temp_1118, temp_1121, temp_1124])
                temp_1150_arv =np.average([temp_7_arv, temp_9_arv, temp_11_arv])

            print(temp_1150_arv)
            plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[8].fSurfTempAct", temp_1150_arv, pyads.PLCTYPE_REAL)
    client.subscribe("raspberry/temperature_array")
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    while not connected:
        time.sleep(0.1)
    while not Message_received:
        time.sleep(0.1)


if __name__ == '__main__':
    while True:
        try:
            run()
        except Exception as e:
            print(e)
            break
