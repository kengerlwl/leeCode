import numpy as  np
from matplotlib import  pyplot
import math
import cmath

xT = np.linspace(0,2 * math.pi, 50)

def calp(xT, n):
    points = []
    for i in xT:
        num = 1 + 1j * (i / n)  # python 可以用这种方式表达复数（1， i/ n）
        num = num ** n
        # print(num)
        points.append(num)
    return points



pyplot.ion()
pyplot.show()


n = 5000
for j in range(1,n, 150):
    nowN = j
    points = calp(xT,nowN)

    # print(points)
    px = []
    py = []
    for i in points:
        x = i.real  # 实部
        y = i.imag # 虚部
        px.append(x)
        py.append(y)
    pyplot.title('the n is ' + str(nowN))
    pyplot.scatter(px, py, c='blue')
    pyplot.plot(px, py, c='green')
    pyplot.pause(0.2)
    pyplot.cla()





