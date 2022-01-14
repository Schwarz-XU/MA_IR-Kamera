# sub.py
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")
    # print(f"Connected with result code {rc}")
    client.subscribe("raspberry/temperature_array")  # sub the topic


payload = bytes()  # initial the payload var. as a empty bytes var.


def on_message(client, userdata, msg):
    # receive the temperature data from broker
    global payload
    payload = msg.payload


def run():
    # establish connection
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.will_set('raspberry/sub/status', b'{"status": "off"}')  # set last will to find out if the program is running
    client.connect('broker.emqx.io', 1883, 60)
    # start the loop
    client.loop_start()
    # client.loop_forever()


if __name__ == '__main__':
    while True:
        run()
