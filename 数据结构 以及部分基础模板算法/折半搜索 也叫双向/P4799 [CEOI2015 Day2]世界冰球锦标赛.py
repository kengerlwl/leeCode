n, m = input().split(' ')

n = int(n)
m = int(m)

s = input().split(' ')
List = []

for i in s:
    List.append(int(i))


class dfs:


    def __init__(self):
        self.val = None
        self.nums= []
        self.ans = []
        self.m = None

    def main(self, val, pos):

        if pos == len(self.nums):
            if val<= self.m:
                self.ans.append(val)
            return

        now = self.nums[pos]

        self.main(val+ now, pos+1)

        self.main(val, pos+1)

mid = len(List) //2
left = List[0:mid]
right = List[mid:len(List)+1]

d =dfs()
d.nums = left
d.m = m
d.main(0, 0)


d2 = dfs()
d2.nums = right
d2.m=m
d2.main(0,0)


l= d.ans
r= d2.ans
r = sorted(r)
import bisect
ans = 0
for i in l:
    target = m - i
    a = bisect.bisect_right(r, target)
    ans+=a
# print(l,r)
print(ans)