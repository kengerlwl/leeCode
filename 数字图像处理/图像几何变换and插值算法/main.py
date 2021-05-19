import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from 数字图像处理.图像几何变换and插值算法.插值算法 import *

im = Image.open('./../image/lena.png')


print(im.size)
img = np.array(im)      # image类 转 numpy


print(img.shape)

img = img[:,:,0:3]

# 变大Magnification 倍得缩放矩阵

# Magnification = 0.3
#
# A= [
#     [Magnification, 0, 0],
#     [0, Magnification, 0],
#     [0, 0, 1],
# ]
# A = np.array(A)
# AI = np.linalg.inv(A)


# 旋转矩阵计算
theta = np.pi / 6

A= [
    [np.cos(theta), np.sin(theta), 0],
    [-1*np.sin(theta), np.cos(theta), 0],
    [0, 0, 1],
]
A = np.array(A)
AI = np.linalg.inv(A)
x0 = [1,2,1]
x0 = np.array(x0).reshape(3,1)


# # 平移矩阵
# A= [
#     [1, 0, 50],
#     [0, 1, 50],
#     [0, 0, 1],
# ]
# A = np.array(A)
# AI = np.linalg.inv(A)




w, h, c = img.shape
newImg = np.zeros((w, h, c))


# 基本的线性插值算法
def linearInterpolation(x0, y0, x1,y1, xn):
    # 原来的256有限制数位的大小，会导致数据溢出
    y0= y0.astype(np.int32)
    y1 = y1.astype(np.int32)
    # 要小心被除数为0
    if x1 -x0 !=0:
        a =  y0 + (y1- y0) * ((xn- x0)/(x1-x0))

        return a
    else:
        return y0




# 双线性插值插值算法
for i in range(int(w )):
    for j in range(int(h)):
        try:

            pointNow = np.array([i, j, 1])
            pointNew = np.dot(AI, pointNow)
            newImg[i][j] = doubleLinearInterpolation(img, pointNew[0],pointNew[1])
        except Exception as e:
            newImg[i][j] = [0,0,0]
            # print(e)



newImg = newImg.astype(np.int32)
print(newImg)
plt.imshow(newImg)
plt.show()