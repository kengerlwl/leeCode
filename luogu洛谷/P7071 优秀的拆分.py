n = input()
n = int(n)
numList =[]
for i in range(1, 10000):
    now = 2**i
    if now > n:
        break

    numList.append(now)

# print(numList)

# 可以暴力
i = len(numList) -1

ans =[]
flag = False
while i >= 0:
    # print(i)
    if n >= numList[i]:
        n -= numList[i]
        ans.append(numList[i])


    if n ==0:
        flag = True
        # print(ans)


    i -=1


if flag:
    for i in ans:
        print(i, end=' ')
    print('')
else:
    print(-1)