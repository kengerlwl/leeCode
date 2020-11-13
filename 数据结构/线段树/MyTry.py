
# 本次以求和为例子
class TreeNode(object):
    def __init__(self, data, l, r): # l , r 的闭区间
        self.left_node = None
        self.right_node = None
        self.l = l
        self.r = r
        mid = (l + r) //2
        self.mid = mid
        self.val = 0
        self.lazyFlag = False
        self.lazyChange = 0

        if l ==r:
            self.val = data[l]
            return None

        print(l, mid, r)
        leftNode = TreeNode(data, l, mid)
        rightNode = TreeNode(data, mid+1, r)



        self.left_node = leftNode
        self.right_node = rightNode

        # 后序遍历
        self.val =  self.left_node.val+self.right_node.val




    # 打印函数
    def __str__(self):
        # return '[%s,%s,] num:%s, %s' % (self.l, self.r, self.num, id(self)) # 查看地址,确实新建了部分节点
        return '\t\t[%s,%s,] num:%s,' % (self.l, self.r, self.val) + '\n'

    # # 打印当前树形结构
    def str_arr(self, level =0):
        # self._show_arr(self)
        if self.lazyFlag or self.lazyChange !=0:
            ret = "|-\t"*level+ "" +str(self.val)+ "  lazy is : " + str(self.lazyChange) + ' flag is  '+str(self.lazyFlag) + "\n"
        else:
            ret = "|-\t"*level+ "" +str(self.val)+ "\n"


        if self.left_node != None:
            ret +=  self.left_node.str_arr(level+1)
        if self.right_node != None:
            ret += self.right_node.str_arr(level+1)
        return ret
        # printTree(self)




    # 区间查询
    def query(self, l, r):
        if self.l == l and self.r == r:
            return self.val

        # 并没有成整的区间, 并且有上次的懒惰，先往下推，先让子区间更新一下
        if self.lazyFlag:
            self.left_node.update(self.l, self.mid, self.lazyChange)
            self.right_node.update(self.mid +1, self.r, self.lazyChange)
            self.lazyChange =0
            self.lazyFlag= False

        leftVal =0
        rightVal=0


        if r <= self.mid:
            leftVal = self.left_node.query(l, r)

        if l >self.mid:
            rightVal = self.right_node.query(l, r)

        if l <= self.mid and r > self.mid:
            if self.left_node != None:
                leftVal = self.left_node.query(l, self.mid)
            if self.right_node != None:
                rightVal = self.right_node.query(self.mid +1, r)

        return leftVal + rightVal




    # 区间修改
    def update(self, l, r, change):


        if self.l == l and self.r == r:  # 如果该区间刚好吻合，那么直接标记该区间就行

            if self.l == self.r:  # 如果为单节点，也就是说，没有叶子节点
                self.lazyChange += change
                self.val += self.lazyChange * (self.r - self.l + 1)
                self.lazyChange  = 0
                self.lazyFlag = False
                return None

            # print('this is the return',l,r)
            self.lazyChange += change
            self.lazyFlag = True
            self.val += self.lazyChange * (self.r - self.l +1)
            return None



        # 并没有刚好匹配的区间, 并且有上次的懒惰，先往子节点计算上次的
        if self.lazyFlag:
            self.left_node.update(self.l, self.mid, self.lazyChange)
            self.right_node.update(self.mid +1, self.r, self.lazyChange)
            self.lazyChange =0
            self.lazyFlag= False




        # 判断应该往哪个子节点走，怎么走区间
        preChange = 0
        if self.lazyFlag: #如果已经有lazy标记了
            self.lazyFlag = False
            preChange = self.lazyChange
            self.lazyChange =0

        if r <= self.mid and self.left_node:
            self.left_node.update(l, r, change + preChange)

        if l >self.mid and self.right_node:
            self.right_node.update(l, r,change+ preChange)

        if l <= self.mid and r > self.mid:
            if self.left_node != None:
                self.left_node.update(l, self.mid, change+ preChange)
            if self.right_node != None:
                self.right_node.update(self.mid +1, r, change+ preChange)



        # 后序遍历， 更新完两个子区间的值后，更新父的区间
        self.val = self.left_node.val + self.right_node.val



if __name__ == '__main__':
    data = [(i+1) for i in range(10)]
    root = TreeNode(data, 0, len(data)-1)
    a = root.str_arr()
    print(a)
    root.update(2, 4, 2)
    a = root.str_arr()
    print(a)
    root.query(0, 0)

    a = root.str_arr()
    print(a)
    # print(root.query(0,3))