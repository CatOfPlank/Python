# -*- coding: utf-8 -*-     # 支持中文
# -*- coding: utf-8 -*-     # 支持中文
import socket
import time
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题
plt.title('归一化幅频特性曲线')
plt.grid(True, which='both', ls='dashed')
plt.xlabel("频率/KHz")
plt.ylabel("归一化幅度/dB")
my_x_ticks = np.arange(0, 220, 10)
plt.xticks(my_x_ticks)
plt.show()
