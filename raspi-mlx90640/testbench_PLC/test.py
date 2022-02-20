# test.py
import time
from queue import Queue
import paho.mqtt.client as mqtt
import pyads

broker_address = "mqtt.eclipseprojects.io"
broker_port = 1883
plc_address = "5.78.127.222.1.1"
plc_port = 851
connected = False
message_received = False

# var. names set
eCtrlMode_dic = {}
fSupTempSet_dic = {}
f2WValveOpenSetMan_dic = {}
b6WValveActivateMan_dic = {}
bPumpActivateMan_dic = {}
wall = {"wall1": Queue(), "wall2": Queue()}
for i in range(0, 15):
    eCtrlMode_dic["eCtrlMode_" + str(i)] = Queue()
    fSupTempSet_dic["fSupTempSet_" + str(i)] = Queue()
    f2WValveOpenSetMan_dic["f2WValveOpenSetMan_" + str(i)] = Queue()
    b6WValveActivateMan_dic["b6WValveActivateMan_" + str(i)] = Queue()
    bPumpActivateMan_dic["bPumpActivateMan_" + str(i)] = Queue()


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


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connect to MQTT broker")
        global connected
        connected = True
    else:
        print(f"Connection fails with result code {rc}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    topic = str(msg.topic)
    if topic == "rkl/test/1":
        print(topic)
        pri_eCtrlMode_dic["CW"].put(int(payload))
        print("CW: " + str(payload))
    elif topic == "rkl/test/2":
        print(topic)
        pri_eCtrlMode_dic["HW"].put(int(payload))
        print("HW: " + str(payload))
    else:
        print("no topic matches, wait for it!")


def plc_write(plc, queue, var_address, var_type):

    if not queue.empty():
        print("queue not empty")
        plc.write_by_name(var_address, queue.get(), var_type)
        print(queue.get())
    else:
        print(f"{queue} is empty")


def run():
    try:
        plc = pyads.Connection(plc_address, plc_port)
        plc.open()
        client = mqtt.Client(clean_session=True)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(broker_address, broker_port, 60)
        client.subscribe("rkl/test/1")
        client.subscribe("rkl/test/2")
        client.loop_start()
        while not connected:
            time.sleep(0.1)
        while not message_received:
            time.sleep(0.1)
        plc_write(plc, pri_eCtrlMode_dic["CW"])
        plc_write(plc, pri_eCtrlMode_dic["HW"])
        client.loop_stop()
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    run()
