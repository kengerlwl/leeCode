s = input()
s = s.split('=')
# print(s)
left = s[0]
right = s[1]
num =None
leftD = None
try:
    num = left[0:len(left)-1]
    leftD = left[len(left) - 1:len(left)]

    num = int(num)
    # print(num)
except:
    num = left[0:len(left)-2]
    leftD = left[len(left) - 2:len(left)]

    num = int(num)
    # print(num)



if len(right) == 3:
    rightD = right[len(right)-2:len(right)]
if len(right) == 2:
    rightD = right[len(right)-1:len(right)]
# print(leftD, rightD)
import math
fun = {
    ('GB', 'MB') : math.pow(2, 10),
    ('GB', 'KB'): math.pow(2, 20),
    ('GB', 'B'): math.pow(2, 30),

    ('MB', 'GB'): math.pow(2, -10),
    ('MB', 'KB'): math.pow(2, 10),
    ('MB', 'B'): math.pow(2, 20),

    ('KB', 'GB'): math.pow(2, -20),
    ('KB', 'MB'): math.pow(2, -10),
    ('KB', 'B'): math.pow(2, 10),

    ('B', 'GB'): math.pow(2, -30),
    ('B', 'MB'): math.pow(2, -20),
    ('B', 'KB'): math.pow(2, -10),
}

ans =None
if leftD == rightD:
    ans= num
else:
    ans = fun[(leftD, rightD)]* num

print('%.6f'%ans)
# 128B=?GB