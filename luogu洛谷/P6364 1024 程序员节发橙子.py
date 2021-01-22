n = input()
n = int(n)


s = input().split(' ')
scores = []
for i in s:
    scores.append(int(i))

# print(scores)

dp1 = [1 for i in range(n)]
i = 0
while i < n-1:
    j = i+1
    if j >= n:
        break
    now = scores[j]
    last = scores[i]
    while now > last:
        dp1[j] = dp1[j-1] +1
        j+=1
        if j >= n:
            break
        now = scores[j]
        last = scores[j-1]

    i = j


scores.reverse()
dp2 = [1 for i in range(n)]
i = 0
while i < n-1:
    j = i+1
    if j >= n:
        break
    now = scores[j]
    last = scores[i]
    while now > last:
        dp2[j] = dp2[j-1] +1
        j+=1
        if j >= n:
            break
        now = scores[j]
        last = scores[j-1]

    i = j

dp2.reverse()
#
# print(dp1)
# print(dp2)



ans = 0
for i in range(len(dp2)):
    ans += max(dp2[i], dp1[i])

print(ans)