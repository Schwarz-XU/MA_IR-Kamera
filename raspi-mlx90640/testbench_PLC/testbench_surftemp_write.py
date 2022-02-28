# testbench_surftemp_write.py
import paho.mqtt.client as mqtt
from datetime import datetime
import numpy as np
import time
import pyads
from DataProcessing.mov_avg import value_moving_avg

connected = False
Message_received = False
broker_address = "broker.emqx.io"
broker_port = 1883
plc_address = "5.78.127.222.1.1"
plc_port = 851
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


def subscribe(client: mqtt):
    plc = pyads.Connection(plc_address, plc_port)
    plc.open()

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
                '''
                # Panel 1110 (not usable)
                temp_2015 = temperature_array[20][15]
                temp_2018 = temperature_array[20][18]
                temp_2021 = temperature_array[20][21]
                temp_2024 = temperature_array[20][24]
                temp_20_arv = np.average([temp_2015, temp_2018, temp_2021, temp_2024])

                # Panel 1120
                temp_1915 = temperature_array[19][15]
                temp_1918 = temperature_array[19][18]
                temp_1921 = temperature_array[19][21]
                temp_1924 = temperature_array[19][24]
                temp_19_arv = np.average([temp_1915, temp_1918, temp_1921, temp_1924])

                # Panel 1130
                temp_1615 = temperature_array[16][15]
                temp_1618 = temperature_array[16][18]
                temp_1621 = temperature_array[16][21]
                temp_1624 = temperature_array[16][24]
                temp_16_arv = np.average([temp_1615, temp_1618, temp_1621, temp_1624])

                # Panel 1140
                temp_1415 = temperature_array[14][15]
                temp_1418 = temperature_array[14][18]
                temp_1421 = temperature_array[14][21]
                temp_1424 = temperature_array[14][24]
                temp_14_arv = np.average([temp_1415, temp_1418, temp_1421, temp_1424])
                '''

                # Panel 1150
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
                temp_1150_arv = np.average([temp_7_arv, temp_9_arv, temp_11_arv])
                temp_1150_arv_10 = value_moving_avg(temp_1150_arv, 10, 0.4).mov_avg()  # current frame rate < 4.0 fps
                '''
                # Panel 1160
                temp_315 = temperature_array[3][15]
                temp_318 = temperature_array[3][18]
                temp_321 = temperature_array[3][21]
                temp_324 = temperature_array[3][24]
                temp_3_arv = np.average([temp_315, temp_318, temp_321, temp_324])
                temp_415 = temperature_array[4][15]
                temp_418 = temperature_array[4][18]
                temp_421 = temperature_array[4][21]
                temp_424 = temperature_array[4][24]
                temp_4_arv = np.average([temp_415, temp_418, temp_421, temp_424])
                temp_1160_arv = np.average([temp_3_arv, temp_4_arv])
                '''
            plc.write_by_name("PRG_WtrSupCC_Zone11.fbPanelSupCtrl.fSurfTempAct", temp_1150_arv_10, pyads.PLCTYPE_REAL)
            plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[8].fSurfTempAct", temp_1150_arv_10, pyads.PLCTYPE_REAL)
    client.subscribe("raspberry/temperature_array")
    client.on_message = on_message


def run():
    try:
        client = connect_mqtt()
        subscribe(client)
        client.loop_start()
        while not connected:
            time.sleep(0.1)
        while not Message_received:
            time.sleep(0.1)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
