import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


im = Image.open('./../image/lena.png')


print(im.size)
img = np.array(im)      # image类 转 numpy


print(img.shape)

img = img[:,:,0:3]




b = img[:,:,0:1]
plt.imshow(img, 'Blues')
plt.show()

plt.savefig('out.png')