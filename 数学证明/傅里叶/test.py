import numpy as np

import matplotlib.pyplot as plt
import math

x = np.linspace(0, 10, 1000)
y = 4 * np.sin(x) / math.pi + 4 * np.sin(3 * x) / math.pi / 3 \
    + 4 * np.sin(5 * x) / math.pi / 5
print('------------')
plt.figure()
plt.plot(x, y)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False
plt.title('傅里叶变换波形')
plt.show()
