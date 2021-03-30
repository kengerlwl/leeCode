class DDstack():
    def __init__(self):
        self.list=[]  # 要注意栈底要垫一个最小/大，预防本身就是最小等情况
        self.cmp = lambda a,b:a[0]>b[0] # 默认递增， 即栈顶最大。 用于找最近小于

    def push(self, num):
        a = []
        while len(self.list) > 0 and ( self.cmp(num,self.list[-1])): # 当 num 不符合栈顶时 ，就出栈
            a.append(self.pop())
        self.list.append(num)
        return a


    def pop(self):
        return self.list.pop()

    def len(self):
        return len(self.list)


    # 返回栈
    def adj(self):
        if self.len() ==1:
            return -1
        else:
            return self.list[1]




class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        tList = []
        for i in range(len(T)):
            tList.append([T[i], i])

        d = DDstack()
        inf = float('INF')
        d.list = [[inf, -1]]
        f = {}
        for i in range(len(T)):
            ans = d.push(tList[i])
            print(d.list)
            for a, b in ans:
                f[b] = tList[i][1]- b


        # print(f)
        ans = []
        for i in range(len(T)):
            if i in f:
                ans.append(f[i])
            else:
                ans.append(0)
        print(ans)

        return ans


Solution.dailyTemperatures(None,[89,62,70,58,47,47,46,76,100,70])

