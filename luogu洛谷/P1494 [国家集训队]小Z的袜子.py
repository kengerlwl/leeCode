n, m = input().split(' ')
n = int(n)
m  =int(m)

nums = input().split(' ')
new = []
for i in nums:
    new.append(int(i))

nums = new

querys =[]
for i in range(m):
    s  = input().split(' ')
    querys.append([int(s[0]), int(s[1]) ])


print(querys)


