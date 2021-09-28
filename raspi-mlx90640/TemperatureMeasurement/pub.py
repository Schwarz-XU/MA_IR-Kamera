# pub.py
import paho.mqtt.client as mqtt
import time
from TemperatureMeasurement import mlx90640


class publisher:

    def publish(self, data):
        
        def on_connect(self, client, userdata, flags, rc):
            print(f"Connected with result code {rc}")
        
        # establish connection
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect("broker.emqx.io", 1883, 60)
        client.publish('raspberry/temperature_array', payload=data[0][0], qos=0, retain=False)
        print(f"send {data[0][0]} data to raspberry/temperature_array")
        time.sleep(2)
        #client.loop_forever()
