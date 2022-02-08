import paho.mqtt.client as mqtt
import pyads


# publisher
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def plc_connect(address):
    plc = pyads.Connection(address, 851)
    plc.open()
    return plc


if __name__ == "__main__":
    plc_address = "5.78.127.222.1.1"
    plc = plc_connect(plc_address)
    while True:
        try:
            # establish connection
            client = mqtt.Client()
            client.on_connect = on_connect
            client.will_set("raspberry/test/status", b'{"status": "off"}', retain=True)  # Set will to find the status of publisher
            client.connect("broker.emqx.io", 1883, 60)  # TODO: free server right now, replace it with institute's server later
            # read data from plc via. pyads
            for i in range(0, 15):
                data = str(plc.read_by_name("GVL_WtrSupCC.stZone11_PanelSup[{nPanelIndex}].fSupTempAct".format(nPanelIndex=i), pyads.PLCTYPE_REAL))
                client.publish('testbench/flowrate/huba', payload=data, qos=0, retain=False)
        except:
            break