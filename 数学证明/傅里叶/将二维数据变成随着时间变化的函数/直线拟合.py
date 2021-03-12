import numpy as np
import path
import matplotlib.pyplot as plt
from 变量存储与加载 import varLD

Funcs = []  # 存储每一段的计算函数
T = None    # 存储一共需要花费的时间， 这里假设每段直线都花费相同的时间1

# 已知两点， 得到函数
def calAtoB(x1, y1, x2, y2):

    # p = (1-t)A + tB #这是点的计算公式,t是比例
    return lambda t: [(1-t) * x1 +t* x2 , (1-t) * y1 +t* y2]


# 最终的函数，随着时间的变化而变化
def Function(t):
    left = t % len(Funcs)

    index = int(left)
    # print(index, len(Funcs))
    tmpF = Funcs[index]

    return tmpF(left % 1)


def calFunc(x ,y):
    print(x[0],y[0])

    # 这里尝试直接直线插值进去的方法。 每个线段的 时间 默认 都是相等的
    plt.plot(x, y)

    length = len(x)
    T = length -1



    for i in range(0, length -1):
        x1 = x[i]
        x2 = x[i+1]
        y1 = y[i]
        y2 = y[i+1]

        f = calAtoB(x1, y1, x2, y2)
        Funcs.append(f)

    testY = []
    testX = []
    t = np.linspace(0, T, 100)

    for nowt in t:
        x, y = Function(nowt)
        testX.append(x)
        testY.append(y)



    plt.scatter(testX, testY)
    plt.show()

x, y =     varLD.loadData(filePath=path.FileDir + '\数学证明\傅里叶\将二维数据变成随着时间变化的函数\date')
x = x - np.mean(x)
y = y - np.mean(y)
calFunc(x,y)
T = len(Funcs)
