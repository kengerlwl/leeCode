import numpy as np


# 临近插值算法
def adjInterpolation(src, x0,y0):
    srcX = round(x0)
    srcY = round(y0)
    return src[srcX][srcY]


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
def doubleLinearInterpolation(src, x0,y0):

    pointNew = [x0,y0]
    srcX = pointNew[0]
    srcY = pointNew[1]
    w, h ,d= src.shape

    # 剔除边界外的点
    if srcX > 0 and srcX < w and srcY > 0 and srcY < h:
        pass
    srcXMin = np.floor(pointNew[0]).astype(np.int32)
    srcYMin = np.floor(pointNew[1]).astype(np.int32)
    srcXMax = np.ceil(pointNew[0]).astype(np.int32)
    srcYMax = np.ceil(pointNew[1]).astype(np.int32)

    yUP = linearInterpolation(srcXMin, src[srcXMin][srcYMax], srcXMax, src[srcXMax][srcYMax], srcX)
    yDOWN = linearInterpolation(srcXMin, src[srcXMin][srcYMin], srcXMax, src[srcXMax][srcYMin], srcX)
    # print(srcX,srcY)
    ans = linearInterpolation(srcYMin, yDOWN, srcYMax, yUP, srcY)
    # print(str(ans))

    return ans
