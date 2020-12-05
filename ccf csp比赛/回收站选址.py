n = input()
n = int(n)

#数据应该是稀疏的
points= {}
for i in range(n):
    s= input().split(' ')
    x = int(s[0])
    y = int(s[1])
    points[(x, y)] = True


# 判断是否可以，计算得分
def judge(x, y):
    xd = [0,0,1,-1]
    yd = [1,-1, 0, 0]
    flag  = True
    for i in range(4):
        tmpx  = x+ xd[i]
        tmpy = y+ yd[i]
        if (tmpx, tmpy) not in points:
            flag= False
            break

    if flag:
        xd = [1, -1, 1, -1]
        yd = [1, -1, -1, 1]
        count =0
        for i in range(4):
            tmpx = x + xd[i]
            tmpy = y + yd[i]
            if (tmpx, tmpy)  in points:
                count +=1

        return count

    else:
        return -1
count =[0 for i in range(5)]
for x, y in points:
    ans = judge(x, y)
    if ans !=-1:
        count[ans] +=1

# print(count)
for i in count:
    print(i)


