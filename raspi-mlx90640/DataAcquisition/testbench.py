import paho.mqtt.client as mqtt
import pyads
from time import time


plc_address = "5.78.127.222.1.1"
plc_port = 851

# publisher
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("rkl/test/write")

write = None

def on_message(client, userdata, msg):
    global write
    # print(f"{msg.topic} {msg.payload}")
    if msg.topic == "rkl/test/write":
        write = int(msg.payload.decode("utf-8"))


if __name__ == "__main__":
    plc = pyads.Connection(plc_address, plc_port)
    plc.open()
    while True:
        try:
            # establish connection
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            # client.will_set("raspberry/test/status", b'{"status": "off"}', retain=True)  # Set will to find the status of publisher
            client.connect("broker.emqx.io", 1883, 60)  # TODO: free server right now, replace it with institute's server later
            client.loop_start()
            if not write == None:
                print(write)
                plc.write_by_name("GVL_WtrSupCC.stZone11_PanelSup[10].eCtrlMode", write, pyads.PLCTYPE_INT)
            else:
                continue
        except Exception:
            plc.close()
            print("Error: error occurs")
            break
