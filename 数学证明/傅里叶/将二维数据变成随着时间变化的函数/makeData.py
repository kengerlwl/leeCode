import numpy as np
import path
import math
from 变量存储与加载 import varLD

# x, y 的参数方程，用来计算在某个时间进度下，x和y的坐标
def fx(t):
    x = 2 * np.cos(t) - np.cos(2*t)
    x = x * 50
    return x
def fy(t):
    y = 2* np.sin(t) - np.sin(2*t)
    y = y * 50
    return y


def ft(t):
    x = fx(t)
    y = fy(t)
    return x + 1j * y



def makeDate():
    t = np.linspace(0, 2 * math.pi, 100)
    x = []
    y = []
    for i in  t:

        x.append(fx(i))
        y.append(fy(i))

    return x, y


if __name__ == '__main__':
    x, y = makeDate()
    varLD.saveData([x, y], filePath=path.FileDir + '\数学证明\傅里叶\将二维数据变成随着时间变化的函数\date')

