import paho.mqtt.client as mqtt
from queue import Queue

'''
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    client.subscribe("rkl/test/1")
    client.subscribe("rkl/test/2")


q = Queue()


def on_message(client, userdata, msg):
    q.put(msg)


while True:
    try:
        client = mqtt.Client(clean_session=True)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("broker.emqx.io", 1883, 60)
        client.loop_start()
        if not q.empty():
           message = q.get()
           print(message.payload)
    except Exception:
        print("Error!")
'''

topic = "Rkl/WtrSup/zone11/panel_1/eCtrlMode"
payload = bytes(11)

var_names = locals()
for i in range(0, 15):
    if topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/eCtrlMode".format(nPanelIndex=i) and payload != bytes():
        var_names["eCtrlMode_" + str(i)] = payload.decode("utf-8")
    elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/fSupTempSet".format(nPanelIndex=i):
        var_names["fSupTempSet_" + str(i)] = float(payload.decode("utf-8"))
    elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/f2WValveOpenSetMan".format(nPanelIndex=i):
        var_names["f2WValveOpenSetMan_" + str(i)] = float(payload.decode("utf-8"))
    elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/b6WValveActivateMan".format(nPanelIndex=i):
        var_names["b6WValveActivateMan_" + str(i)] = bool(payload.decode("utf-8"))
    elif topic == "Rkl/WtrSup/zone11/panel_{nPanelIndex}/bPumpActivateMan".format(nPanelIndex=i):
        var_names["bPumpActivateMan_" + str(i)] = bool(payload.decode("utf-8"))
print(var_names["eCtrlMode_" + str(i)])
