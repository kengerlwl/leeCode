class node():
    def __init__(self):
        self.parent =None
        self.chrldren = {}  #不重复的子节点， 而且索引效率高
        self.val = None


    def show(self, deep=0):

        print(deep * '--' , end=' ')
        print(self.val)
        for i in self.chrldren:
            child = self.chrldren[i]
            child.show(deep +2)


    # 前， 中， 后 序遍历树, 这里是前序
    def travel(self):

        print(self.val)
        for i in self.chrldren:
            child = self.chrldren[i]
            child.travel()





    #插入节点， 用层级关系， val作为纽带
    def __insert(self, List, position=1):
        #到了最后一个节点
        if position == len(List):
            return


        now = List[position]

        # 已经存在就继续递进
        if now in self.chrldren:
            self.chrldren[now].__insert(List, position +1)

        # 不存在，先创建，再继续
        elif now not in self.chrldren:
            tmp = node()
            tmp.val = now
            tmp.parent = self

            self.chrldren[now] = tmp
            self.chrldren[now].__insert(List, position +1)




    def insert(self, List):

        #root 存在值
        if self.val:
            if self.val == List[0]:
                self.__insert(List, position=1)
            else:
                print('根节点对不上')
        else:
            self.val = List[0]
            self.insert(List)


    def delete(self, List):
        pass






if __name__ == '__main__':
    tree = node()
    import random
    for i in range(20):
        a = [random.randint(0,10) for i in range(5)]
        tree.insert(a)
        tree.show()