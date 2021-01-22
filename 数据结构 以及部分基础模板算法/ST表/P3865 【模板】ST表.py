import math

n, m = input().split(' ')
n = int(n)
m = int(m)

#这里统一转化到下标为正常
List  = [0]
s= input().split(' ')

for i in s:
    if i.isdigit():
        List.append(int(i))


# st[i][j] 从i开始的2^j个中间的max
st = [ [0 for i in range(20) ] for i in range(n+2)]

for i in range(1, n+1):
    st[i][0] = List[i]

t =math.log(n) / math.log(2) + 1
t = math.floor(t)
for j in range(1, t):
    for i in range(1, n- (1 << j) +2):
        st[i][j] = max(st[i][j-1], st[i + (1 << (j-1))][j-1])  #分为左右两个区间取最大值



for i in range(m):
    l, r = input().split(' ')
    l = int(l)
    r  = int(r)
    k  = (r - l +1)

    k = math.log(k) / math.log(2)
    k = math.floor(k)
    ans = max(st[l][k], st[r - (1<<k)+1][k])
    print(ans)



