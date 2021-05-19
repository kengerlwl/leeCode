# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取原始图像
img = cv2.imread('./../image/grayLena.png')

# 图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 获取图像高度和宽度
height = grayImage.shape[0]
width = grayImage.shape[1]

# 创建一幅图像
result = np.zeros((height, width), np.uint8)

k = 1
b = 50

def f1(x):
    return x*x


def f2(x):
    return 1 * x - 50

def f3(x):
    return np.log(1 + x) * 30

# 图像灰度上移变换 DB=DA+50
for i in range(height):
    for j in range(width):
        res = f2(grayImage[i,j])
        if (int(res) > 255):
            gray = 255
        elif (int(res) < 0):
            gray = 0
        else:
            gray = int(res)

        result[i, j] = np.uint8(gray)

# 显示图像
cv2.imshow("Gray Image", grayImage)
cv2.imshow("Result", result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
