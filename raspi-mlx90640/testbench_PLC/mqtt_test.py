import paho.mqtt.client as mqtt
import time
from datetime import datetime
from queue import Queue

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
P1140_SurfTemp_G = float()


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            global connected
            connected = True
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt.Client(clientid = "Rkl_TwinCAT", clean_session=True)
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
        global P1140_SurfTemp_G
        topic = str(msg.topic)
        payload = msg.payload.decode("utf-8")
        print(datetime.now().strftime("%H:%M:%S"))
        print(f"Received `{payload}` from `{topic}` topic")
        if topic == "raspberry/temperature_(20;14)":
            P1110_SurfTemp.put(float(payload))
        elif topic == "raspberry/temperature_(19;14)":
            P1120_SurfTemp.put(float(payload))
        elif topic == "raspberry/temperature_(17;14)":
            P1130_SurfTemp.put(float(payload))
        elif topic == "raspberry/temperature_(15;14)":
            P1140_SurfTemp.put(float(payload))
            P1140_SurfTemp_G = float(payload)
        elif topic == "raspberry/temperature_(10;14)":
            P1150_SurfTemp.put(float(payload))
        elif topic == "raspberry/temperature_(5;14)":
            P1160_SurfTemp.put(float(payload))
        else:
            print("no topic matches, check the subscription")
        #plc_write(plc, queue=P1110_SurfTemp, var_address="GVL_WtrSupCC.stZone11_PanelSup[4].fSurfTempAct", var_type=pyads.PLCTYPE_REAL)
        #plc_write(plc, queue=P1120_SurfTemp, var_address="GVL_WtrSupCC.stZone11_PanelSup[5].fSurfTempAct", var_type=pyads.PLCTYPE_REAL)
        #plc_write(plc, queue=P1130_SurfTemp, var_address="GVL_WtrSupCC.stZone11_PanelSup[6].fSurfTempAct", var_type=pyads.PLCTYPE_REAL)
        # plc_write(plc, queue=P1140_SurfTemp, var_address="GVL_WtrSupCC.stZone11_PanelSup[7].fSurfTempAct", var_type=pyads.PLCTYPE_REAL)
        plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[7].fSurfTempAct", P1140_SurfTemp_G, pyads.PLCTYPE_REAL)
        #plc_write(plc, queue=P1150_SurfTemp, var_address="GVL_WtrSupCC.stZone11_PanelSup[8].fSurfTempAct", var_type=pyads.PLCTYPE_REAL)
        #plc_write(plc, queue=P1160_SurfTemp, var_address="GVL_WtrSupCC.stZone11_PanelSup[9].fSurfTempAct", var_type=pyads.PLCTYPE_REAL)
    #client.subscribe("raspberry/temperature_(20;14)")
    #client.subscribe("raspberry/temperature_(19;14)")
    #client.subscribe("raspberry/temperature_(17;14)")
    client.subscribe("raspberry/temperature_(15;14)")
    #client.subscribe("raspberry/temperature_(10;14)")
    #client.subscribe("raspberry/temperature_(5;14)")
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    while not connected:
        time.sleep(0.1)


if __name__ == '__main__':
    while True:
        try:
            run()
        except Exception as e:
            print(e)
            break
