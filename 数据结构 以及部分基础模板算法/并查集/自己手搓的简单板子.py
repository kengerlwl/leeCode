
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

if __name__ == '__main__':
    bq = BQSet()
    for i in range(10):
        bq.f[i] =i

    bq.f[2] =1
    a= bq.judge(1,2)
    bq.Union(2,3)
    print(a)