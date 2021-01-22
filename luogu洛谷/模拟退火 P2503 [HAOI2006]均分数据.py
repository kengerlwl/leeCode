INF= float("INF")
import math
import copy
import random

def rand():
    return random.randint(0, 32767)
maxR  = 32767

eps = math.e**(-15)
r=0.99
num=[0 for i in range(30)]
be = copy.deepcopy(num)  # belong
Sum = copy.deepcopy(num)
ave = 0
ans = math.e**(15)
def find_min(Sum):
    ans  = 1
    minV = INF
    for i in range(1, m+1):
        if Sum[i] < minV:
            minV = Sum[i]
            ans = i
    return ans

n=None
m =None


def sa():
    Sum = [0 for i in range(30)]
    be =[0 for i in range(30)]
    ans = 0
    T = 10005
    for i in range(1, n+1): # 每个人随机分配到一组中去
        be[i] = rand() % m +1
        Sum[be[i]] += num[i]  # 计算该组的和
    # print(be, '\n',Sum)


    for i in range(1, m+1):   # 计算均方差
        # print(ave)
        ans+= (Sum[i] - ave)**2

    while T > eps:
        p = find_min(Sum)  # 找到最小的那个
        # print(p)

        x = rand() % n +1  # 随机选出一个数字 ,加入到最小组

        newSum = copy.deepcopy(Sum)

        newSum[be[x]] -= num[x]
        newSum[p] += num[x]
        newA = 0
        for i in range(1, m + 1):  # 计算均方差
            newA += (newSum[i] - ave)**2

        if newA < ans or (math.exp(ans - newA) / T) * rand() < maxR:
            be[x] = p
            Sum = copy.deepcopy(newSum)
            ans = newA
        else:
            pass
        # print(ans)
        # print(be)
        # print(Sum)
        T *= r  # 不断降温
    return ans




n,m = input().split(' ')
n = int(n)
m = int(m)
s = input().split(' ')
for index,i in enumerate(s):
    num[index+1] = int(i)
ave = sum(num) / m

fin = INF
for i in range(100):
    a = sa()
    if a < fin:
        # print('good',a)
        fin = a
    else:
        pass
        # print('not good',a)
print(fin)