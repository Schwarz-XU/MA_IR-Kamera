import paho.mqtt.client as mqtt
import time
from TemperaturMeasurment import mlx90640


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


print("pub.py is running")
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

while True:
    data = mlx90640.plot_update()
    for i in range(5):
        client.publish('raspberry/temperature_array', payload=i, qos=0, retain=False)
        print(f"send {len(data)} data to raspberry/topic")
        time.sleep(1)

client.loop_forever()
