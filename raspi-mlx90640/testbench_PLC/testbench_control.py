# testbench_control.py
import paho.mqtt.client as mqtt
import pyads
from queue import Queue

plc_address = "5.78.127.222.1.1"
plc_port = 851
broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883

# var. names set
# pri. side
pri_eCtrlMode_dic = {"CW": Queue(), "HW": Queue()}
pri_fCircSupTempSet_dic = {"CW": Queue(), "HW": Queue()}
pri_fMixingValveOpenSetMan_dic = {"CW": Queue(), "HW": Queue()}
pri_fPumpPowerSetMan_dic = {"CW": Queue(), "HW": Queue()}

# sec. side
sec_eCtrlMode_dic = {"CW": Queue(), "HW": Queue()}
sec_fCircSupTempSet_dic = {"CW": Queue(), "HW": Queue()}
sec_fValveOpenSetMan_dic = {"CW": Queue(), "HW": Queue()}
sec_fPumpPowerSetMan_dic = {"CW": Queue(), "HW": Queue()}

# wall
wall_eCtrlMode_dic = {"Wall_10XX": Queue(), "Wall_11XX": Queue(), "Wall_12XX": Queue()}
# panel
panel_eCtrlMode_dic = {}
panel_fSupTempSet_dic = {}
panel_f2WValveOpenSetMan_dic = {}
panel_b6WValveActivateMan_dic = {}
panel_bPumpActivateMan_dic = {}
for i in range(0, 15):
    panel_eCtrlMode_dic["eCtrlMode_" + str(i)] = Queue()
    panel_fSupTempSet_dic["fSupTempSet_" + str(i)] = Queue()
    panel_f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(i)] = Queue()
    panel_b6WValveActivateMan_dic["b6WValveActivateMan_" + str(i)] = Queue()
    panel_bPumpActivateMan_dic["bPumpActivateMan_" + str(i)] = Queue()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    # subscribe the topic
    # pri. side
    # cold water
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/fCircSupTempSet")
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/fMixingValveOpenSetMan")
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/fPumpPowerMan")
    # hot water
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/fCircSupTempSet")
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/fMixingValveOpenSetMan")
    client.subscribe("Rkl/WtrSup/zone11/pri_hw/fPumpPowerSetMan")

    # sec. side
    # cold water
    client.subscribe("Rkl/WtrSup/zone11/sec_cw/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/sec_cw/fCircSupTempSet")
    client.subscribe("Rkl/WtrSup/zone11/sec_cw/fValveOpenSetMan")
    client.subscribe("Rkl/WtrSup/zone11/sec_cw/fPumpPowerSetMan")
    # hot water
    client.subscribe("Rkl/WtrSup/zone11/sec_hw/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/sec_hw/fCircSupTempSet")
    client.subscribe("Rkl/WtrSup/zone11/sec_hw/fValveOpenSetMan")
    client.subscribe("Rkl/WtrSup/zone11/sec_hw/fPumpPowerSetMan")

    # wall
    client.subscribe("Rkl/WtrSup/zone11/wall_10XX/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/wall_11XX/eCtrlMode")
    client.subscribe("Rkl/WtrSup/zone11/wall_12XX/eCtrlMode")
    # panel
    for j in range(0, 15):
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=j))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=j))
        # manual mode
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=j))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=j))
        client.subscribe("Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=j))


def on_message(client, userdata, msg):
    payload = msg.payload
    topic = str(msg.topic)
    print(payload)
    print(topic)
    # Zone 11
    # put command into queue
    # pri. side
    # cold water
    if topic == "Rkl/WtrSup/pri_cw/eCtrlMode":
        pri_eCtrlMode_dic["CW"].put(int(payload))
    elif topic == "Rkl/WtrSup/pri_cw/fCircSupTempSet":
        pri_fCircSupTempSet_dic["CW"].put(float(payload))
    elif topic == "Rkl/WtrSup/pri_cw/fMixingValveOpenSetMan":
        pri_fMixingValveOpenSetMan_dic["CW"].put(float(payload))
    elif topic == "Rkl/WtrSup/pri_cw/fPumpPowerSetMan":
        pri_fPumpPowerSetMan_dic["CW"].put(float(payload))
    # hot water
    elif topic == "Rkl/WtrSup/pri_hw/eCtrlMode":
        pri_eCtrlMode_dic["HW"].put(int(payload))
    elif topic == "Rkl/WtrSup/pri_hw/fCircSupTempSet":
        pri_fCircSupTempSet_dic["HW"].put(float(payload))
    elif topic == "Rkl/WtrSup/pri_hw/fMixingValveOpenSetMan":
        pri_fMixingValveOpenSetMan_dic["HW"].put(float(payload))
    elif topic == "Rkl/WtrSup/pri_hw/fPumpPowerSetMan":
        pri_fPumpPowerSetMan_dic["HW"].put(float(payload))
    # sec. side
    # cold water
    elif topic == "Rkl/WtrSup/zone11/sec_cw/eCtrlMode":
        sec_eCtrlMode_dic["CW"].put(int(payload))
    elif topic == "Rkl/WtrSup/zone11/sec_cw/fCircSupTempSet":
        sec_fCircSupTempSet_dic["CW"].put(float(payload))
    elif topic == "Rkl/WtrSup/zone11/sec_cw/fValveOpenSetMan":
        sec_fValveOpenSetMan_dic["CW"].put(float(payload))
    elif topic == "Rkl/WtrSup/zone11/sec_cw/fPumpPowerSetMan":
        sec_fPumpPowerSetMan_dic["CW"].put(float(payload))
    # hot water
    elif topic == "Rkl/WtrSup/zone11/sec_hw/eCtrlMode":
        sec_eCtrlMode_dic["CW"].put(int(payload))
    elif topic == "Rkl/WtrSup/zone11/sec_hw/fCircSupTempSet":
        sec_fCircSupTempSet_dic["CW"].put(float(payload))
    elif topic == "Rkl/WtrSup/zone11/sec_hw/fValveOpenSetMan":
        sec_fValveOpenSetMan_dic["CW"].put(float(payload))
    elif topic == "Rkl/WtrSup/zone11/sec_hw/fPumpPowerSetMan":
        sec_fPumpPowerSetMan_dic["CW"].put(float(payload))
    # wall
    elif topic == "Rkl/WtrSup/zone11/wall_10XX/eCtrlMode":
        wall_eCtrlMode_dic["Wall_10XX"].put(int(payload))
    elif topic == "Rkl/WtrSup/zone11/wall_11XX/eCtrlMode":
        wall_eCtrlMode_dic["Wall_11XX"].put(int(payload))
    elif topic == "Rkl/WtrSup/zone11/wall_12XX/eCtrlMode":
        wall_eCtrlMode_dic["Wall_12XX"].put(int(payload))
    else:
        for k in range(0, 15):
            if topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=k):
                panel_eCtrlMode_dic["eCtrlMode_" + str(k)].put(int(payload))
            elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=k):
                panel_fSupTempSet_dic["fSupTempSet_" + str(k)].put(float(payload))
            elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=k):
                panel_f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(k)].put(float(payload))
            elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=k):
                panel_b6WValveActivateMan_dic["b6WValveActivateMan_" + str(k)].put(bool(payload))
            elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=k):
                panel_bPumpActivateMan_dic["bPumpActivateMan_" + str(k)].put(bool(payload))
            else:
                print("waiting for message from broker")


# TODO: Version 1 of write into plc
def plc_write(my_plc):
    # Zone 11
    # Panel control parameter write via. pyads
    for index in range(0, 15):
        if not panel_eCtrlMode_dic["eCtrlMode_" + str(index)].empty():
            my_plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].eCtrlMode".format(panel_index=index),
                                 panel_eCtrlMode_dic["eCtrlMode_" + str(index)].get_nowait(),
                                 pyads.PLCTYPE_INT)
            print(
                my_plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].eCtrlMode".format(panel_index=index),
                                    pyads.PLCTYPE_INT))
        if not panel_fSupTempSet_dic["fSupTempSet_" + str(index)].empty():
            my_plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].fSupTempSet".format(panel_index=index),
                                 panel_eCtrlMode_dic["fSupTempSet_" + str(index)].get_nowait(),
                                 pyads.PLCTYPE_REAL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].fSupTempSet".format(panel_index=index),
                pyads.PLCTYPE_REAL))
        if not panel_f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(index)].empty():
            my_plc.write_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].f2WValveOpenSetMan".format(panel_index=index),
                panel_eCtrlMode_dic["f2WValveOpenSetMan_" + str(index)].get_nowait(),
                pyads.PLCTYPE_REAL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].f2WValveOpenSetMan".format(panel_index=index),
                pyads.PLCTYPE_REAL))
        if not panel_b6WValveActivateMan_dic["b6WValveActivateMan_" + str(index)].empty():
            my_plc.write_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].b6WValveActivateMan".format(panel_index=index),
                panel_eCtrlMode_dic["b6WValveActivateMan_" + str(index)].get_nowait(),
                pyads.PLCTYPE_BOOL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].b6WValveActivateMan".format(panel_index=index),
                pyads.PLCTYPE_BOOL))
        if not panel_bPumpActivateMan_dic["bPumpActivateMan_" + str(index)].empty():
            my_plc.write_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].bPumpActivateMan".format(panel_index=index),
                panel_eCtrlMode_dic["bPumpActivateMan_" + str(index)].get_nowait(),
                pyads.PLCTYPE_BOOL)
            print(my_plc.read_by_name(
                "GVL_WtrSupCC.stZone11_PanelSup[{panel_index}].bPumpActivateMan".format(panel_index=index),
                pyads.PLCTYPE_BOOL))


# TODO: Version 2 of write into PLC: use the following function
def write_plc(plc, queue, data_address, data_type):
    if not queue.empty():
        plc.write_by_name(data_address, queue.get(), data_type)
        print(plc.read_by_name(data_address, data_type))


def run():
    plc = pyads.Connection(plc_address, plc_port)
    plc.open()
    try:
        client = mqtt.Client(clean_session=True)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(broker_address, broker_port, 60)
        client.loop_start()
        for pri_index in range(1, 2):
            write_plc(plc, pri_eCtrlMode_dic["CW"], "GVL_WtrSupPri.stWtrSupPri[1].eCtrlMode", pyads.PLCTYPE_INT)

        # plc_write(plc)
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    run()
