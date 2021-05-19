import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from 数字图像处理.图像几何变换and插值算法.插值算法 import *




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


# 透视变换
def warpPerspective(src, A):
    AI = np.linalg.inv(A)
    w, h, c = src.shape
    newImg = np.zeros((w, h, c))

    for i in range(int(w)):
        for j in range(int(h)):
            try:

                pointNow = np.array([i, j, 1])
                tmpVecter = np.dot(AI, pointNow)
                tmpVecter = tmpVecter / tmpVecter[2]
                # exit()
                pointNew = tmpVecter


                # print(tmpVecter, pointNew)


                newImg[i][j] = adjInterpolation(src, pointNew[0],pointNew[1])
            except Exception as e:
                newImg[i][j] = [0,0,0]
    return newImg

