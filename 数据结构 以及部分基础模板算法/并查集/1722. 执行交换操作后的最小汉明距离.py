
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

        if self.f[a] == self.f[b]:
            return True
        else:
            return False

    def Union(self,source, a):
        a = self.getFather(a)
        sF = self.getFather(source)
        self.f[a] = sF

class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        bq = BQSet()
        length = len(source)
        for i in range(length):
            bq.f[i] = i
        for a, b in allowedSwaps:
            bq.Union(a, b)

        f = {}
        for i in bq.f:

            father = bq.getFather(i)
            if father not in f:
                f[father] = [i]
            else:
                f[father].append(i)

        def cal(tmp):
            s = {}
            t = {}
            for i in tmp:
                if source[i] not in s:
                    s[source[i]] = 1
                else:
                    s[source[i]] += 1
                if target[i] not in t:
                    t[target[i]] = 1
                else:
                    t[target[i]] += 1

            print(s, t)

            ans  = 0
            for i in t:
                if i  in s:
                    a = t[i]
                    b = s[i]
                    if a >= b:
                        ans+= b
                    else:
                        ans +=a
            return len(tmp) - ans


        re = 0
        for i in f:
            print(f[i])
            tmp = f[i]
            t = cal(tmp)
            re+=t

        print(re)
        return re



Solution.minimumHammingDistance(None,[2,3,1],
[1,2,2],
[[0,2],[1,2]])

