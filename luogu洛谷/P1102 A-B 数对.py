n , c = input().split(' ')

n = int(n)
c = int(c)


s = input().split()

news = []
count ={}
for i in s:
    tmp = int(i)
    if tmp not in count:
        count[tmp]  =1
    else:
        count[tmp] +=1

# print(count)


index = sorted(count)
# print(index)

ans = 0
for i in index:
    target =  i -c
    # print(target)
    if target in count:
        ans += count[i] * count[target]





print(ans)