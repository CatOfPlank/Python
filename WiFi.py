"""
Wifi数据传输---服务端

"""
# -*- coding: utf-8 -*-     # 支持中文
import socket
import time
import matplotlib.pyplot as plt
import numpy as np

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
amp_num = 10     # 纵坐标数据量


def Receive():
    data = client_socket.recv(9)  # 收到9个字节
    data = data.decode('gbk')
    data = str(data[0:5])   # 去掉回车换行和空格
    f_data = data.replace("\\", "").replace("r", "").replace("n", "").lstrip('0')  # 去掉特殊符号
    f_data = float(f_data)
    data_buff.append(f_data)
    data_buff_normalize = []    # 归一化幅度
    # 接收到的信息，一个字节
    if len(data_buff) >= amp_num:  # 收到足够的数据后绘图
        max_value = max(data_buff)  # 求列表最大值
        for i in range(0, amp_num):
            data_buff_normalize.append(20*np.log(data_buff[i]/max_value))
        draw(data_buff_normalize)
        data_buff.clear()  # 清空

# 画曲线


def draw(data):
    freq = np.linspace(0, 200, 10)  # 频率轴
    plt.xlabel("Frequency/KHz")
    plt.ylabel("Normalization/dB")
    plt.plot(freq, data, color='red')
    plt.show()


if __name__ == '__main__':
    while True:
        Receive()
        time.sleep(0.2)
