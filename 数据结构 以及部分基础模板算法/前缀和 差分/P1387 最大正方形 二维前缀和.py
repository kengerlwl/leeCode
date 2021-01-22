# 二维上的前缀和

n, m = input().split(' ')

n = int(n)
m = int(m)

matrix = []
for i in range(n):
    s = input().split(' ')
    tmp = []
    for i in s:
        tmp.append(int(i))
    matrix.append(tmp)

preSum = [ [0 for i in range(m) ] for i in range(n) ]

preSum[0][0] = matrix[0][0]
for i in range(1,n):
    preSum[i][0] = matrix[i][0] + preSum[i-1][0]

for i in range(1,m):
    preSum[0][i] = matrix[0][i] + preSum[0][i-1]


for i in range(1,n):
    for j in range(1, m):
        preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1] + matrix[i][j]


def cal(x1,y1, x2, y2):
    return preSum[x2][y2] - preSum[x1][y2] - preSum[x2][y1] + preSum[x1][y1], (y2 - y1) * (x2 - x1)






def check(mid):

    pass


minV = 1
maxV = min(n, m)

l = minV
r = maxV

while l < r:
    mid = (l +r) //2
    if check(mid):
        l = mid
    else:
        r= mid

