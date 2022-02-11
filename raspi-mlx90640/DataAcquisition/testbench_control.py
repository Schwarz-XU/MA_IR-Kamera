# testbench_control.py
import paho.mqtt.client as mqtt
import pyads
import traceback
import logging


plc_address = "5.78.127.222.1.1"
plc_port = 851
broker_address = "broker.emqx.io"
broker_port = 1883


def plc_connect(address, port):
    plc = pyads.Connection(address, port)
    plc.open()
    return plc


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    # subscribe the topic
    # Zone 11
    # Panel control parameter write via. pyads
    for i in range(0, 15):
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=i))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=i))
        # manual mode
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=i))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=i))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=i))


def on_message(client, userdata, msg):
    var_names = globals()
    for i in range(0, 15):
        if msg.topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=i):
            var_names["eCtrlMode_" + str(i)] = int(msg.payload.decode("utf-8"))
        elif msg.topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=i):
            var_names["fSupTempSet_" + str(i)] = int(msg.payload.decode("utf-8"))
        elif msg.topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=i):
            var_names["f2WValveOpenSetMan_" + str(i)] = float(msg.payload.decode("utf-8"))
        elif msg.topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=i):
            var_names["b6WValveActivateMan_" + str(i)] = bool(msg.payload.decode("utf-8"))
        elif msg.topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=i):
            var_names["bPumpActivateMan_" + str(i)] = bool(msg.payload.decode("utf-8"))
        print(var_names["eCtrlMode_" + str(i)])

def run():
    # rkl_plc = plc_connect(plc_address, plc_port)
    # print("this is running")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, broker_port, 60)
    client.loop_forever()


if __name__ == "__main__":
    run()
    # rkl_plc = pyads.Connection(plc_address, plc_port)
