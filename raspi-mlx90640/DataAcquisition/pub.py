# pub.py
import numpy as np
import paho.mqtt.client as mqtt
import time


class publisher:

    def publish(self, data):
        
        def on_connect(self, client, userdata, flags, rc):
            print(f"Connected with result code {rc}")
        data_str = np.array2string(data, precision=2, separator=",", formatter={'float_kind': lambda x: "%.2f"% x})
        # establish connection
        client = mqtt.Client()
        client.on_connect = on_connect
        client.connect("broker.emqx.io", 1883, 60)
        client.publish('raspberry/temperature_array', payload=data_str, qos=0, retain=False)
        print(f"send {data_str} data to raspberry/temperature_array")
        time.sleep(2)


if __name__ == '__main__':
    while True:
        run()
