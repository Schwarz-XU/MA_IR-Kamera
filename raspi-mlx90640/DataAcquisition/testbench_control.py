# testbench_control.py
import paho.mqtt.client as mqtt
import pyads


plc_address = "5.78.127.222.1.1"
plc_port = 851
broker_address = "broker.emqx.io"
broker_port = 1883

payload = bytes()
topic = ""


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
    global payload
    global topic
    payload = msg.payload
    topic = msg.topic
    print(payload
          )


def plc_write(address, port):
    # plc = pyads.Connection(address, port)
    # plc.open()
    var_names = locals()
    for i in range(0, 15):
        if topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=i):
            var_names["eCtrlMode_" + str(i)] = int(payload.decode("utf-8"))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=i):
            var_names["fSupTempSet_" + str(i)] = float(payload.decode("utf-8"))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=i):
            var_names["f2WValveOpenSetMan_" + str(i)] = float(payload.decode("utf-8"))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=i):
            var_names["b6WValveActivateMan_" + str(i)] = bool(payload.decode("utf-8"))
        elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=i):
            var_names["bPumpActivateMan_" + str(i)] = bool(payload.decode("utf-8"))
        print(var_names["eCtrlMode_" + str(i)])


def run():
    # print("this is running")
    # plc_write(plc_address, plc_port)
    plc_write(plc_address, plc_port)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_address, broker_port, 60)
    client.loop_forever()


if __name__ == "__main__":
    try:
        run()
    except Exception:
        print("Error: errors occur")
