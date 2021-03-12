import numpy as np
import path
import matplotlib.pyplot as plt

Funcs = []  # 存储每一段的计算函数
T = None    # 存储一共需要花费的时间， 这里假设每段直线都花费相同的时间1

# 已知两点， 得到函数
def calAtoB(x1, y1, x2, y2):

    # p = (1-t)A + tB #这是点的计算公式,t是比例
    return lambda t: [(1-t) * x1 +t* x2 , (1-t) * y1 +t* y2]


# 最终的函数，随着时间的变化而变化
def Function(t):
    left = t % len(Funcs)
    # print(t, left)
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

    # print(Funcs)

    testY = []
    testX = []
    t = np.linspace(0, T, 100)

    for nowt in t:
        x, y = Function(nowt)
        testX.append(x)
        testY.append(y)



    plt.scatter(testX, testY)
    plt.show()

trDatas = []#临时容器

import re
trDatas = []#临时容器
points = []
center = [500,500]#中心点位置

with open(path.FileDir + '\数学证明\傅里叶\将二维数据变成随着时间变化的函数\\rawvertexes.txt', 'r') as f:  # 读取并解析SVG信息
    rawdata = f.readlines()
    curve = re.sub(r'\s', '', "".join(rawdata))
    cells = re.findall(r'\w[\d\,\-\.]+', curve)
    for cell in cells:
        trcdata = []
        formatString = re.sub(r'-', ',-', cell)
        trcdata.append(re.match(r'[A-Za-z]', formatString).group(0))
        rawvers = re.sub(r'[A-Za-z]\,?', '', formatString).split(',')
        for st in range(len(rawvers)):
            rawvers[st] = float(rawvers[st])
        vergroup = []
        vercurgrp = []
        for st in range(len(rawvers)):
            vercurgrp.append(rawvers[st])
            if len(vercurgrp) >= 2:
                vergroup.append(vercurgrp[0] + vercurgrp[1] * 1j)
                vercurgrp.clear()
        if len(vercurgrp) > 0:
            if re.match(r'v', trcdata[0], re.I):
                vergroup.append(0 + vercurgrp[0] * 1j)
            elif re.match(r'h', trcdata[0], re.I):
                vergroup.append(vercurgrp[0] + 0j)
        trcdata.append(vergroup)
        trDatas.append(trcdata)
    print('Vertexes data have been read.')

for i in range(1, len(trDatas)):  # 解析SVG信息
    if re.match(r'[a-z]', trDatas[i][0]):
        for j in range(len(trDatas[i][1])):
            trDatas[i][1][j] += trDatas[i - 1][1][-1]
for i in range(len(trDatas)):  # 解析SVG信息
    flag = trDatas[i][0]
    if re.match(r'm', flag, re.I): continue
    trDatas[i][1].insert(0, trDatas[i - 1][1][-1])
    if re.match(r's', flag, re.I):
        trDatas[i][1].insert(1, 2 * trDatas[i - 1][1][-1] - trDatas[i - 1][1][-2])
    if re.match(r'[lvh]', flag, re.I):
        trDatas[i][1].insert(1, trDatas[i][1][0] / 3 + trDatas[i][1][-1] * 2 / 3)
        trDatas[i][1].insert(1, trDatas[i][1][0] * 2 / 3 + trDatas[i][1][-1] / 3)

for i in range(len(trDatas)):  # 解析SVG信息
    flag = trDatas[i][0]
    if re.match(r'm', flag, re.I): continue
    points.append(trDatas[i][1])
for i in range(len(points)):  # 将中心点归零
    for j in range(len(points[i])):
        points[i][j] -= center[0] + 1j * center[1]



print(points)
x = []
y = []
for i in  points:
    print(i)
    i = i[0]
    x.append(i.real)
    y.append(-1 * i.imag)
print(x, y)
calFunc(x,y)
T = len(Funcs)
