
#encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./../image/grayLena.png',cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(img)

cv2.imshow("src", img)
cv2.imshow("result", equ)

plt.hist(img.ravel(), 256)
plt.figure()
plt.hist(equ.ravel(), 256)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

