"""
Wifi数据传输---服务端

"""
import sys
import socket
import time
import  re
import matplotlib.pyplot as plt
import threading
import struct
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# socket
# 地址和端口号
address = ('192.168.0.171', 8080)
# 创建一个socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定
tcp_server_socket.bind(address)

# listen里的数字表征同一时刻能连接客户端的程度.
tcp_server_socket.listen(5)

client_socket, clientAddr = tcp_server_socket.accept()
print("等待客户端连接...")
if clientAddr is not None:
    print("连接成功！")

# 接收数据
data_buff = []


def Receive():
    data = client_socket.recv(3)    # 收到一个字节

    data = str(data)
    f_data = data.replace("\\" , "").replace("r","").replace("n","")
    f_data = float(f_data)
    data_buff.append(f_data)
    # 接收到的信息，一个字节
    if len(data_buff) >= 5:  # 收到足够的数据后绘图
        draw(data_buff)
        data_buff.clear()  # 清空


# 画曲线
def draw(data):
    freq = np.linspace(0, 200, 200)  # 频率轴
    plt.plot(freq, data)


if __name__ == '__main__':
    while True:
        Receive()
        time.sleep(0.2)
