n, m  = input().split(' ')
n = int(n)
m = int(m)

Cmatrix = [[0 for i in range(1+n)] for i in range(2+n)]
preSum = [[0 for i in range(1+n)] for i in range(2+n)]

def show(m):
    for i in m:
        print(i)

    print('\n\n')
points = []

for i in range(m):
    s  = input().split(' ')
    x1 = int(s[0])
    y1 = int(s[1])

    x2 = int(s[2])
    y2= int(s[3])

    for y in  range(y1, y2+1):
        Cmatrix[x1][y] += 1


    for y in range(y1, y2+1):
        Cmatrix[x2+1][y] -= 1



# show(Cmatrix)





for y in range(1, n+1):
    sum = 0
    for x in range(1, n+1):
        sum+= Cmatrix[x][y]
        preSum[x][y] = sum

# show(preSum)


for x in range(1, n+1):
    for y in range(1, n+1):
        print(preSum[x][y], end=' ')
    print()