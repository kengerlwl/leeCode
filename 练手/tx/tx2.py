str = input().split(' ')
for i in range(len(str)):
    str[i] = int(str[i])
import math

n = str[0]
u = str[1]
v =str[2]
s = str[3]
t =str[4]
m = str[5]

flag1 = v - 2 * u
a = t
b = -1 * 2 * s
c = s * n - m
f = b * b / (4 * a* a) - c /a

x1 = -1 * b / (2 * a) + math.sqrt(f)
x2 = -1 * b / (2 * a) - math.sqrt(f)

# print(x1, x2)
def judge(y):
    if s * (n -  2 * y) + t * y *y <= m:
        return True
    else:
        return False
def calA(y):
    return u * (n - 2 * y) + v * y

if  flag1 ==0:
    print(v*n)
elif flag1 > 0:  # 递增 xiao
    if x2 > 0:
        y = math.floor(x2)
    else:
        y = 0
    # print(y)
    print(calA(y))
else:
    # print(2)
    y = int(x1)
    print(calA(y))
