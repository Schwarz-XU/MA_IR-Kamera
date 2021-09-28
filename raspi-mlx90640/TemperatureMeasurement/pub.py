# pub.py
import paho.mqtt.client as mqtt
import time
from TemperatureMeasurement import mlx90640
# from TemperatureMeasurement import test
# import sys, os

# add TemperatureMeasurement module path
# sys.path.append("/home/pi/MA_IR-Kamera/raspi-mlx90640")


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


print("pub.py is running")
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

client.publish('raspberry/temperature_array', payload=mlx90640.plot_update()[0], qos=0, retain=False)
print(f"send {mlx90640.plot_update()[0]} data to raspberry/temperature_array")
time.sleep(2)        
client.loop_forever()

# while True:
#     data = mlx90640.plot_update()
#     # data = [0, 1]
#     client.publish('raspberry/temperature_array', payload=data[0], qos=0, retain=False)
#     print(f"send {data} data to raspberry/temperature_array")
#
#     time.sleep(2)



