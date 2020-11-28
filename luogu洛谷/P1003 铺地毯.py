n = input()
n = int(n)


#转化数据类型为int
def change(numList):
    ans =[]
    for i in numList:
        ans.append(int(i))
    return ans

ans =[]
for i in range(n):
    tmp = input().split(' ')
    ans.append(change(tmp))

x, y = input().split(' ')
x = int(x)
y = int(y)

def judge(matrix, x, y):
    if x>=matrix[0] and x <=matrix[0] + matrix[2]:
        if y >= matrix[1] and y <= matrix[1] + matrix[3]:
            return True
    else:
        return False

flag = True
for i in range(len(ans)-1, -1, -1):
    # print(ans[i])
    if judge(ans[i], x, y):
        print(i +1)
        flag = False
        break


if flag:
    print(-1)

