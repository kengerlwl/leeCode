import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


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
theta = np.pi / 4

A= [
    [np.cos(theta), np.sin(theta), 0],
    [-1*np.sin(theta), np.cos(theta), 0],
    [0, 0, 1],
]
A = np.array(A)
AI = np.linalg.inv(A)
x0 = [1,2,1]
x0 = np.array(x0).reshape(3,1)


w, h, c = img.shape
newImg = np.ones((w, h, c))

def linearInterpolation(x0, y0, x1,y1, xn):
    return y0 + (y1- y0) * [(x1 - x0) /(xn- x0)]


w, h, c = img.shape
newImg = np.ones((w, h, c))

# 临近插值算法
def doubleLinearInterpolation(src, x0,y0):
    srcX = round(x0)
    srcY = round(y0)
    return src[srcX][srcY]


for i in range(int(w )):
    for j in range(int(h )):
        try:
            pointNow = np.array([i, j, 1])
            pointNew = np.dot(AI, pointNow)
            newImg[i][j] = doubleLinearInterpolation(img, pointNew[0], pointNew[1])
        except Exception as e:
            print(e)

newImg = newImg.astype(np.int32)
plt.imshow(newImg)
# plt.show(0)


newImg = newImg.astype(np.int32)
print(newImg)
plt.imshow(newImg)
plt.show()
