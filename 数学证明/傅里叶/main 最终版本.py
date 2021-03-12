# 相对于原来的数据，这里已经能够读取离散的数据，然后进行模拟了。
# plus最终版本中，把数据颠倒进行拟合

import numpy as np
import matplotlib.pyplot as plt
import math


import 数学证明.傅里叶.将二维数据变成随着时间变化的函数.直线拟合 as Fun

# x, y = varLD.loadData(filePath=path.FileDir + '\数学证明\傅里叶\将二维数据变成随着时间变化的函数\date')

# Fun.calFunc(x, y)

def ft(t):
    x, y = Fun.Function(t)
    return x + 1j * y * -1

t= np.linspace(0, 2 * math.pi, 100)

# # 验证一下函数的有效性,并且这段不能省略，否则数据加载不出来
testY = []
testX = []
t = np.linspace(0,len(Fun.Funcs) , 100)

for nowt in t:
    x, y = Fun.Function(nowt)
    testX.append(x)
    testY.append(y)

plt.plot(testX, testY)



# plt.show()



# 开始计算傅里叶

# 微分计算的步长
dx = 0.01
T = Fun.T  # 周期1
wo = 2 * math.pi / T

# 这里用得是欧拉公式化简后的 e 的指数形式
c = []  # 参数c
fc ={}  # 参数c
n = 50  # 2n个圆圈
# 这里的范围就相当于是圈数

# 计算定积分, dx是微分程度， left， right是上下界
def calF(f, dx, left, right):
    Sum = 0


    # 选值进行计算的点
    xNum = np.linspace(left, right, int((right-left) /dx))

    for i in xNum:
        now = f(i) * dx
        Sum += now
    return Sum






for i in range(-1 * n,n +1):
    print(i)
    tmpf = lambda x: ft(x)* np.exp(-1j * i * wo * x)  # 隐函数表达式

    nowc = calF(tmpf, dx, 0, T) / T  # 定积分计算， 因为具有着正交的性质
    c.append([i, nowc])
    fc[i] = nowc


print(c)
# 打印数据
with open("datas.txt", "w") as File:  # 把结果写入文件
    for index in range(n+1):

        a = fc[index]
        b = fc[-1 * index]


        File.write("[{:.5f},{:.5f}],".format(b.real,  b.imag))
        File.write("\n")
        # print(index)
        if index ==0:
            continue # 0不需要两个
        # print(index)

        File.write("[{:.5f},{:.5f}],".format(a.real, a.imag))
        File.write("\n")

# 计算傅里叶级数的函数
def FinallFunc(t):
    Sum = 0
    for n, nowc in c:
        tmp = nowc * np.exp(1j * n * wo * t)
        Sum += tmp

    return Sum



# 进行测试， 看是否计算出来了傅里叶级数
tx = []
ty = []
for i in t:
    num = FinallFunc(i)
    tx0 = num.real
    ty0 = num.imag

    tx.append(tx0)
    ty.append(ty0 * -1)
plt.title('the Fourier data')
plt.scatter(tx, ty, c= 'black')
plt.show()

