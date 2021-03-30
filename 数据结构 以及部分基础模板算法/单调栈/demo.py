class DDstack():
    def __init__(self):
        self.list = []  # 要注意栈底要垫一个最小/大，预防本身就是最小等情况
        self.cmp = lambda a, b: a > b  # 默认递增， 即栈顶最大。 用于找最近小于

    def push(self, num):
        a = []
        while len(self.list) > 0 and (self.cmp(num, self.list[-1])):  # 当 num 不符合栈顶时 ，就出栈
            a.append(self.pop())
        self.list.append(num)
        return a

    def pop(self):
        return self.list.pop()

    def len(self):
        return len(self.list)

    # 返回栈
    def adj(self):
        if self.len() == 1:
            return -1
        else:
            return self.list[1]


d = DDstack()

d.list=[100]# 设置栈底
d.push(1)
print(d.list)

d.push(2)
print(d.list)

d.push(0)
print(d.list)
print(d.adj())
