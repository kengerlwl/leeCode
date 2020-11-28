n, x, y = input().split(' ')
n = int(n)
x = int(x)
y = int(y)

points =[]
for i in range(n):
    s = input().split(' ')
    points.append((int(s[0]), int(s[1])))

ans = []
import math
def dis(x0, y0):
    a = (x - x0)**2 + (y-y0)**2
    return math.sqrt(a)

for i in range(len(points)):
    x0 , y0 = points[i]
    ans.append([dis(x0,y0),i+1])

ans = sorted(ans)
# print(ans)
for i in range(3):
    print(ans[i][1])
