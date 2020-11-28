# 转化数据类型为int
def change(numList):
    ans = []
    for i in numList:
        try:
            ans.append(int(i))
        except:
            pass
    return ans


# 生成某个固定大小得恒值矩阵
def getNumMatrix(rows, columns,value = 0):
    ans = [[value for i in range(columns+5)] for i in range(rows+5)]
    return ans


n= int(input())
matrix = getNumMatrix(value=0, rows=n,columns=n)

while True:
    s = input()

    if s == '0 0  0':
        break

    s =s.split(' ')
    s = change(s)
    # print(s)

    if s == [0, 0, 0]:
        break


    matrix[s[0]][s[1]] = s[2]

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(matrix[i][j], end=' ')
#     print()
#



def getMatrix(deep,length):
    if deep != 1:
        return [getMatrix(deep -1, length) for i in range(length)]
    else:
        return [0 for i in range(length)]

# dp = [[[[0 for i in range(n + 1)] for j in range(n + 1)] for x in range(n + 1)] for y in range(n + 1)]

dp = getMatrix(4,n+1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                dp[i][j][x][y] = max(dp[i - 1][j][x - 1][y], dp[i][j - 1][x - 1][y], dp[i - 1][j][x][y - 1],
                                     dp[i][j - 1][x][y - 1]) + matrix[i ][j ] + matrix[x ][y ]
                if i == x and j == y:
                    dp[i][j][x][y] -= matrix[i][j]
print(dp[n][n][n][n])
