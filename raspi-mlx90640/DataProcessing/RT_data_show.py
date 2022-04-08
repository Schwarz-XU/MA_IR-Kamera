import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 设置样式
plt.style.use('fivethirtyeight')
x_vars = []
y_vars = []


# 定义函数读取csv文件内容
def animate(i):
    # data = pd.read_csv('data.csv')
    data = pd.read_csv('../Data/temperature_data.csv')
    x = data["Time"]
    y1 = data["pos_0_0"]
    y2 = data["pos_0_9"]
    # x = data['x_value']
    # y1 = data['total_1']
    # y2 = data['total_2']

    plt.cla()
    # 绘制线图
    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.legend(loc='upper left')
    plt.tight_layout()


# 调用FuncAnimation实时调用函数每秒执行1次
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
