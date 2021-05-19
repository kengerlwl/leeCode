import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import  copy

im = Image.open('./../image/lena.png')


print(im.size)
img = np.array(im)      # image类 转 numpy


print(img.shape)

img = img[:,:,0:3]


plt.imshow(img)

plt.show()


newImg =  copy.deepcopy(img)
newImg[0:100, 0:100,:] = np.zeros((100,100,3))
plt.imshow(newImg)
plt.show()

