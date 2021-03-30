n = input()
n = int(n)

a = []
b = input().split(' ')

for i in b:
    a.append(int(i))



# print(a)

inf = float('INF')
dp = [0 for i in range(n+1)]
dp[0] = 0

def findIndex(i, time):
    i = i-1
    start = a[i]
    while i >= 0:
        if start - a[i]>=time:
            return i +1
        else:
            i-=1
    return -1

for i in range(1, n+1):
    nowTime = a[i-1]


    # 选择直接付费
    one = dp[i-1] + 20

    # 选择50元得套餐
    f1 = findIndex(i, 100)
    if f1 ==-1:
        two = 50
    else:
        two = 50 + dp[f1]

    # 选择100元得套餐
    f2 = findIndex(i, 1000)
    # print(f2, a[i-1])
    if f2 == -1:
        three = 100
    else:
        three = 100 + dp[f2]

    # print(one, two, three)
    dp[i] = min(one, two, three)


# print(dp)
ans = []
for i in range(1, n+1):
    ans.append(dp[i] - dp[i-1])

# print(ans)


for i in ans:
    print(i)