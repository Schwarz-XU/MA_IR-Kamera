# testbench_control.py
import paho.mqtt.client as mqtt
import pyads
from queue import Queue

plc_address = "5.78.127.222.1.1"
plc_port = 851
broker_address = "broker.emqx.io"
broker_port = 1883

# var. names set
eCtrlMode_dic = {}
fSupTempSet_dic = {}
f2WValveOpenSetMan_dic = {}
b6WValveActivateMan_dic = {}
bPumpActivateMan_dic = {}
eCtrlMode_wall_dic = {"Wall_10XX":Queue(), "Wall_11XX":Queue(), "Wall_12XX":Queue()}

for i in range(0, 15):
    eCtrlMode_dic["eCtrlMode_" + str(i)] = Queue()
    fSupTempSet_dic["fSupTempSet_" + str(i)] = Queue()
    f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(i)] = Queue()
    b6WValveActivateMan_dic["b6WValveActivateMan_" + str(i)] = Queue()
    bPumpActivateMan_dic["bPumpActivateMan_" + str(i)] = Queue()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    # subscribe the topic
    client.subscribe("Rkl/WtrSup/zone11/wall_10XX/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/wall_11XX/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/wall_12XX/eCtrlMode")
    for j in range(0, 15):
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=j))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=j))
        # manual mode
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=j))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=j))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=j))


def on_message(client, userdata, msg):
    payload = msg.payload
    topic = msg.topic
    print(payload)
    print(topic)
    # Zone 11
    # Put command into queue

    if topic == "Rkl/WtrSup/zone11/wall_10XX/eCtrlMode":
        eCtrlMode_wall_dic["Wall_10XX"].put(int(payload.decode("utf-8"))) 
    if topic == "Rkl/WtrSup/zone11/wall_11XX/eCtrlMode":
        eCtrlMode_wall_dic["Wall_11XX"].put(int(payload.decode("utf-8"))) 
    if topic == "Rkl/WtrSup/zone11/wall_12XX/eCtrlMode":
        eCtrlMode_wall_dic["Wall_12XX"].put(int(payload.decode("utf-8"))) 
    for k in range(0, 15):
        if topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=k):
            eCtrlMode_dic["eCtrlMode_" + str(k)].put(int(payload.decode("utf-8")))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=k):
            fSupTempSet_dic["fSupTempSet_" + str(k)].put(float(payload.decode("utf-8")))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=k):
            f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(k)].put(float(payload.decode("utf-8")))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=k):
            b6WValveActivateMan_dic["b6WValveActivateMan_" + str(k)].put(bool(payload.decode("utf-8")))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=k):
            bPumpActivateMan_dic["bPumpActivateMan_" + str(k)].put(bool(payload.decode("utf-8")))
        else:
            print("Panel_{Panel_Index} waits for message from broker".format(Panel_Index=k))


def plc_write(my_plc):
    # Zone 11
    # Panel control parameter write via. pyads
    for index in range(0, 15):
        if not eCtrlMode_dic["eCtrlMode_" + str(index)].empty():
            my_plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].eCtrlMode".format(panel_index=index),
                                 eCtrlMode_dic["eCtrlMode_" + str(index)].get_nowait(),
                                 pyads.PLCTYPE_INT)
            print(my_plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].eCtrlMode".format(panel_index=index),
                                      pyads.PLCTYPE_INT))
        if not fSupTempSet_dic["fSupTempSet_" + str(index)].empty():
            my_plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].fSupTempSet".format(panel_index=index),
                                 eCtrlMode_dic["fSupTempSet_" + str(index)].get_nowait(),
                                 pyads.PLCTYPE_REAL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].fSupTempSet".format(panel_index=index),
                pyads.PLCTYPE_REAL))
        if not f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(index)].empty():
            my_plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].f2WValveOpenSetMan".format(panel_index=index),
                                 eCtrlMode_dic["f2WValveOpenSetMan_" + str(index)].get_nowait(),
                                 pyads.PLCTYPE_REAL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].f2WValveOpenSetMan".format(panel_index=index),
                pyads.PLCTYPE_REAL))
        if not b6WValveActivateMan_dic["b6WValveActivateMan_" + str(index)].empty():
            my_plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].b6WValveActivateMan".format(panel_index=index),
                                 eCtrlMode_dic["b6WValveActivateMan_" + str(index)].get_nowait(),
                                 pyads.PLCTYPE_BOOL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].b6WValveActivateMan".format(panel_index=index),
                pyads.PLCTYPE_BOOL))
        if not bPumpActivateMan_dic["bPumpActivateMan_" + str(index)].empty():
            my_plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].bPumpActivateMan".format(panel_index=index),
                                 eCtrlMode_dic["bPumpActivateMan_" + str(index)].get_nowait(),
                                 pyads.PLCTYPE_BOOL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].bPumpActivateMan".format(panel_index=index),
                pyads.PLCTYPE_BOOL))


def run():
    plc = pyads.Connection(plc_address, plc_port)
    plc.open()
    client = mqtt.Client()
    client.on_connect = on_connect
    try:
        client.on_message = on_message
        client.connect(broker_address, broker_port, 60)
        client.loop_start()
        plc_write(plc)
    except Exception:
        print("Error: Some Errors occur!")


if __name__ == "__main__":
    run()
