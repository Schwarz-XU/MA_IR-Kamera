import paho.mqtt.client as mqtt
import time
from TemperatureMeasurement import mlx90640
# from TemperatureMeasurement import test


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


print("pub.py is running")
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

while True:
    data = mlx90640.plot_update()
    client.publish('raspberry/temperature_array', payload=data, qos=0, retain=False)
    print(f"send {data} data to raspberry/topic")
    time.sleep(2)

client.loop_forever()
