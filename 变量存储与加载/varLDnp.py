import numpy as np
x =[i for i in range(100)]
np.save('x.npy', x)

b = np.load('x.npy')
print(b)