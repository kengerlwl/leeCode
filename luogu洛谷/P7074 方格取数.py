n, m = input().split(' ')
m  = int(m)
n = int(n)

INF  = float('INF')

matric = []
for i in range(n):
    s = input().split(' ')
    tmp =[]
    for j in s:
        tmp.append(int(j))
    matric.append(tmp)

# print(matric)

note ={}



def dfs(i, j, dir): #通过向哪个方向到达当前位置的

    if (i, j, dir) in note:
        return note[(i, j, dir)]


    if i ==0 and j ==0:
        return matric[0][0]
    if not (0<=i and i <n and j >=0 and j <m):
        return -INF

    if dir == 'up':
        up =-INF
        left= -INF
        # print(up, left)

        if 0 <= i - 1 < n:
            up = dfs(i-1, j, dir = 'up')

        if 0 <= j - 1 < m:
            left = dfs(i, j - 1, dir = 'left')
        # print(i, j)
        # print(matric[i][j])
        # print(up, left)
        note[(i, j, dir)] =  matric[i][j] + max(up, left)
        return matric[i][j] + max(up, left)

    elif dir =='down':
        down =-INF
        left= -INF
        if 0<=i+1 < m:
            down = dfs(i+1, j, dir='down')

        if 0<=j-1<m:

            left = dfs(i, j - 1, dir = 'left')
        note[(i, j, dir)] = matric[i][j] + max(down, left)

        return matric[i][j] + max(down, left)

    elif dir =='left':
        up =-INF
        down =-INF
        left= -INF
        if 0 <= i - 1 < n:
            up = dfs(i-1, j, dir = 'up')

        if 0<=i+1 < n:
            down = dfs(i+1, j, dir='down')

        if 0<=j-1<m:
            left = dfs(i, j - 1, dir = 'left')
        note[(i, j, dir)] = matric[i][j] + max(down, left, up)


        return matric[i][j] + max(down, left, up)



a = dfs(n-1, m-1, 'up')
b = dfs(n-1, m-1 , 'left')

print(max(a, b))
