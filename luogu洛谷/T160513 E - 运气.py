n, k = input().split(' ')
n = int(n)
k = int(k)
def isOK(num):
    s = str(num)
    f = True
    for i in s:
        if int(i) >6 or int(i)<1 :
            f = False
            break
    return f


epoch = 10**n
epoch = epoch // k
minv = '1'*n
minv= int(minv)
minv = minv // k
ans  = 0
l = []
for i in range(minv, epoch):
    now = i*k
    # print(now)
    if isOK(now):
        ans+=1
        l.append(now)
print(ans %(10**9 +7))
print(l)

