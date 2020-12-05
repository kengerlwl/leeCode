n , a, b = input().split(' ')
n = int(n)
a = int(a)
b  =int(b)

Vector={}
for i in range(a):
    s = input().split(' ')
    if int(s[0]) not in Vector:
        Vector[int(s[0])] = [int(s[1])]

bV =[]
for i in range(b):
    s = input().split(' ')
    if int(s[0])  in Vector:
        bV.append([int(s[1]), Vector[int(s[0])][0]])



# print(Vector)

ans =0
for i in bV:
    ans += i[0] * i[1]
print(ans)

# 2 2 2
# 1 1
# 2 2
# 1 1
# 2 2