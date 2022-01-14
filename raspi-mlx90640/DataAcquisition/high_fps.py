# high_fps.py
import board
import busio
import time
import adafruit_mlx90640
import numpy as np
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
from scipy import ndimage

# establish I2C bus
i2c = busio.I2C(board.SCL, board.SDA, frequency=1000000)  # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c)  # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ  # set refresh rate
# mlx90640 build
mlx_shape = (24, 32)  # mlx90640 shape
# mlx_interp_val = 10  # interpolate (on each dimension)
mlx_interp_val = 1  # no interpolation
mlx_interp_shape = (mlx_shape[0] * mlx_interp_val,
                    mlx_shape[1] * mlx_interp_val)  # new shape

# set plot
fig = plt.figure(figsize=(1, 1))  # start figure
ax = fig.add_subplot(111)  # add subplot
fig.subplots_adjust(0.05, 0.05, 0.95, 0.95)  # get rid of unnecessary padding
therm1 = ax.imshow(np.zeros(mlx_interp_shape), interpolation='none',
                   cmap=plt.cm.bwr, vmin=25, vmax=45)  # preemptive image

fig.canvas.draw()  # draw figure to copy background
ax_background = fig.canvas.copy_from_bbox(ax.bbox)  # copy background
frame = np.zeros(mlx_shape[0] * mlx_shape[1])  # 768 pts


def plot_update():
    fig.canvas.restore_region(ax_background)  # restore background
    mlx.getFrame(frame)  # read mlx90640
    data_array_raw = np.fliplr(np.reshape(frame, mlx_shape))  # reshape, flip data
    data_array_raw[23][31] = (data_array_raw[22][31]
                              + data_array_raw[23][30]
                              + data_array_raw[22][30]) / 3  # fix error pixel with the average value of nearst
    data_array_raw = ndimage.zoom(data_array_raw, mlx_interp_val)  # interpolate
    return data_array_raw


# publisher
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


# establish connection
client = mqtt.Client()
# client.username_pw_set(username="UEl-Rkl_Tm", password="12345678")  # TODO: not usable, need correction (A: need TSL/SSL)
client.on_connect = on_connect
client.will_set("raspberry/pub/status", b'{"status": "off"}', retain=True)  # Set will to find the status of publisher
client.connect("broker.emqx.io", 1883, 60)  # TODO: free server right now, replace it with institute's server later


def run():
    t_array = []

    while True:
        t1 = time.monotonic()  # for determining frame rate
        try:
            plot_update()  # update plot
            data_array_raw = plot_update()

            # send all data_array to the broker
            data_array_str = np.array2string(data_array_raw, precision=2, separator=",",
                                             formatter={'float_kind': lambda x: "%.2f" % x})
            client.publish('raspberry/temperature_array', payload=data_array_str, qos=0, retain=False)
            # TODO: update picked pixel for each element
            # Temperature on element 1160
            client.publish('raspberry/temperature_(5;8)', payload=data_array_raw[5][8], qos=0, retain=True)
            client.publish('raspberry/temperature_(5;14)', payload=data_array_raw[5][14], qos=0, retain=True)
            client.publish('raspberry/temperature_(5;20)', payload=data_array_raw[5][20], qos=0, retain=True)
            client.publish('raspberry/temperature_(5;26)', payload=data_array_raw[5][26], qos=0, retain=True)
            # Temperature on element 1150
            client.publish('raspberry/temperature_(10;8)', payload=data_array_raw[10][8], qos=0, retain=True)
            client.publish('raspberry/temperature_(10;14)', payload=data_array_raw[10][14], qos=0, retain=True)
            client.publish('raspberry/temperature_(10;20)', payload=data_array_raw[10][20], qos=0, retain=True)
            client.publish('raspberry/temperature_(10;26)', payload=data_array_raw[10][26], qos=0, retain=True)
            # Temperature on element 1140
            client.publish('raspberry/temperature_(15;8)', payload=data_array_raw[15][8], qos=0, retain=True)
            client.publish('raspberry/temperature_(15;14)', payload=data_array_raw[15][14], qos=0, retain=True)
            client.publish('raspberry/temperature_(15;20)', payload=data_array_raw[15][20], qos=0, retain=True)
            client.publish('raspberry/temperature_(15;26)', payload=data_array_raw[15][26], qos=0, retain=True)
            # Temperature on element 1130
            client.publish('raspberry/temperature_(17;8)', payload=data_array_raw[17][8], qos=0, retain=True)
            client.publish('raspberry/temperature_(17;14)', payload=data_array_raw[17][14], qos=0, retain=True)
            client.publish('raspberry/temperature_(17;20)', payload=data_array_raw[17][20], qos=0, retain=True)
            client.publish('raspberry/temperature_(17;26)', payload=data_array_raw[17][26], qos=0, retain=True)
            # Temperature on element 1120
            client.publish('raspberry/temperature_(19;8)', payload=data_array_raw[19][8], qos=0, retain=True)
            client.publish('raspberry/temperature_(19;14)', payload=data_array_raw[19][14], qos=0, retain=True)
            client.publish('raspberry/temperature_(19;20)', payload=data_array_raw[19][20], qos=0, retain=True)
            client.publish('raspberry/temperature_(19;26)', payload=data_array_raw[19][26], qos=0, retain=True)
            # Temperature on element 1110
            client.publish('raspberry/temperature_(20;8)', payload=data_array_raw[20][8], qos=0, retain=True)
            client.publish('raspberry/temperature_(20;14)', payload=data_array_raw[20][14], qos=0, retain=True)
            client.publish('raspberry/temperature_(20;20)', payload=data_array_raw[20][20], qos=0, retain=True)
            client.publish('raspberry/temperature_(20;26)', payload=data_array_raw[20][26], qos=0, retain=True)

            print(f"send {data_array_str} to raspberry/temperature_array")
        except:
            continue

        # approximating frame rate
        t_array.append(time.monotonic() - t1)
        if len(t_array) > 10:
            t_array = t_array[1:]  # recent times for frame rate approx
        print('Frame Rate: {0:2.1f}fps'.format(len(t_array) / np.sum(t_array)))


if __name__ == '__main__':
    while True:
        run()
