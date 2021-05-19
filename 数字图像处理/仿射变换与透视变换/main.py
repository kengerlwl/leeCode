import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from 数字图像处理.图像几何变换and插值算法.插值算法 import *
from 数字图像处理.仿射变换与透视变换.透视变换 import *



im = Image.open('./../image/test01.jpg')


print(im.size)
img = np.array(im)      # image类 转 numpy

plt.imshow(img)
plt.show()
# exit()
print(img.shape)

img = img[:,:,0:3]

# 变大Magnification 倍得缩放矩阵

Magnification = 0.3

A= [
    [Magnification, 0, 0],
    [0, Magnification, 0],
    [0, 0, 1],
]
A = np.array(A)
AI = np.linalg.inv(A)


#获取图像大小
rows, cols = img.shape[:2]
#根据四个顶点设置图像透视变换矩阵
pos1 = np.float32([[114, 82], [287, 156], [8, 322], [216, 333]])  # 原来的坐标
pos2 = np.float32([[0, 0], [188, 0], [0, 262], [188, 262]])    # 变换后的坐标

# 实际肉眼看上去的x，y和数组的存储是有区别的
def exchangeXY(pos):
    for i in range(len(pos)):
        pos[i] = [pos[i][1], pos[i][0]]

exchangeXY(pos1)
exchangeXY(pos2)

# 计算透视变换矩阵
def getPerspectiveTransform(pos1, pos2):
    length = len(pos1)
    tmpMatrix = []
    b = []
    for i in range(length):
        x0, y0 = pos1[i]
        xn, yn = pos2[i]
        tmpMatrix.append(
            [x0, y0,1,0,0,0,-1 * x0 * xn, -1 * y0 * xn]
        )
        tmpMatrix.append(
            [0,0,0,x0, y0,1,-1 * x0 * yn, -1 * y0 * yn]
        )

        b.append(xn)
        b.append(yn)


    tmpMatrix= np.array(tmpMatrix)
    b = np.array(b)
    ans =np.dot(np.linalg.inv(tmpMatrix), b)
    finalMatrix = [
        [ans[0], ans[1], ans[2]],
        [ans[3], ans[4], ans[5]],
        [ans[6], ans[7], 1]

    ]
    return np.array(finalMatrix)

M = getPerspectiveTransform(pos1, pos2)




print(M)
t = np.dot(M, [216, 333,1])
print(t / t[2])
# exit()

A = M


w, h, c = img.shape
newImg =  warpPerspective(img, M)








newImg = newImg.astype(np.int32)
# print(newImg)
plt.imshow(newImg)
plt.show()