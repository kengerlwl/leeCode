c = input()

c = int(c)

import math
def getb(a):
    return (math.sqrt(c**2 - a**2))
for i in range(1,c):
    bo = getb(i)
    b = int(bo)
    # print(b)
    # print(bo - b)
    if b**2 + i**2 == c**2 and bo - b == 0:
        print(i, b)
        break