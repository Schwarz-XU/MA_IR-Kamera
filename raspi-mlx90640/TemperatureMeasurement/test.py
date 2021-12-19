# test.py
import random
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    client.subscribe("test/a")

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")
        
        
client = mqtt.Client()
# client = mqtt.Client()
client.username_pw_set(username="test_name", password= "12345678")
client.on_connect = on_connect
client.on_message = on_message

client.will_set("test/status", b'{"status": "off"}')
client.connect("broker.emqx.io", 1883, 60)
client.loop_forever()


"""
def test(value):
    i = random.random()
    data = [value, value + 2, value + i]
    return data
"""
