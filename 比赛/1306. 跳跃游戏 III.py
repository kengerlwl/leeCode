
class BQSet():
    def __init__(self):
        self.f = {}  # f[i]代表i的父节点
        # #init
        # for i in range(10):
        #     f[i] = i

    def getFather(self,origin):
        a = origin
        while self.f[a] != a:
            a = self.f[a]
        self.f[origin] = a  # 优化一下
        return a

    # 只需要看a， b 是否 有共同父节点
    def judge(self,a, b):
        a  = self.getFather(a)
        b = self.getFather(b)

        return self.f[a] == self.f[b]

    def Union(self,source, a):
        a = self.getFather(a)
        sF = self.getFather(source)
        self.f[a] = sF



class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        bq = BQSet()
        length = len(arr)
        for i in range(length):
            bq.f[i] = i
        queue = [start]
        f= {}
        while queue:

            pos = queue.pop()
            if pos >=  length or pos < 0:
                continue
            f[pos] = True
            now = arr[pos]
            # print(pos, now)
            dis = [-now, now]

            for i in dis:
                next = pos + i
                if next not  in f:
                    queue.append(next)

        flag = False
        for index, i in enumerate(arr):
            if i == 0:
                if index in f:
                    flag = True
                    break

        # print(target)
        return flag

a  = Solution.canReach(None,[0,3,0,6,3,3,4],
6)
print(a)
