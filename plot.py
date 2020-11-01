from matplotlib import pyplot
import numpy as np

data = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
data = np.array(data)
print(data.shape)

x = data[:, 0]
y = data[:, 1]
y0 = [1 for i in range(len(data))]
pyplot.scatter(x, y0)
pyplot.show()