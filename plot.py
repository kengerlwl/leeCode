from matplotlib import pyplot
import numpy as np


#瞄点
# data = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# data = np.array(data)
# print(data.shape)
#
# x = data[:, 0]
# y = data[:, 1]
# y0 = [1 for i in range(len(data))]
# pyplot.scatter(x, y0)
# pyplot.show()


heights = [4,2,7,6,9,14,12]
pyplot.bar(height=heights, x=[i for i in range(len(heights))])
pyplot.show()