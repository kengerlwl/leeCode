s= input().split(' ')
l = int(s[0])
n = int(s[1])
m = int(s[2])


List = [0]
for i in range(n):
    s= input()
    s = int(s)
    List.append(s)

List.append(l)

INF =float('INF')

Dis=[]
minV = INF
for i in range(1, len(List)):
    Dis.append(List[i] - List[i-1])
    minV = min(minV,List[i] - List[i-1])

# print(List)
# print(Dis)
import copy
originD= copy.deepcopy(Dis)


maxV  = l


def judge(mid):
    count= 0
    Dis = copy.deepcopy(originD)
    for i in range(len(Dis)):
        now = Dis[i]
        # print(now, Dis)
        if now < mid:
            count+=1
            if i==len(Dis)-1:
                break
            Dis[i+1] += now

    return count


import math

l = minV

r = maxV
while l < r:
    mid  = (l +r) /2
    mid = math.ceil(mid)

    ans = judge(mid)
    # print(l, r, mid, ans)

    if ans <=m:  #ok
        l=mid
    else:
        r= mid-1

print(l)
