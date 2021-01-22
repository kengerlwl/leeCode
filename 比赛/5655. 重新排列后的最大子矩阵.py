class DDstack():
    def __init__(self):
        self.list=[]  # 要注意栈底要垫一个最小/大，预防本身就是最小等情况
        self.cmp = lambda a,b:a>b # 默认递增， 即栈顶最大。 用于找最近小于

    def push(self, num):
        while len(self.list) > 0 and (not self.cmp(num,self.list[-1])): # 当 num 不符合栈顶时 ，就出栈
            self.pop()
        self.list.append(num)

    def pop(self):
        return self.list.pop()

    def len(self):
        return len(self.list)

    def adj(self):
        if self.len() ==1:
            return -1
        else:
            return self.list[ len(self.list) -2]




class Solution1:
    def largestRectangleArea(self, heights):

        a = heights
        d = DDstack()
        d.cmp = lambda a, b:a[0] > b[0]
        l1 = []
        d.list=[ [-1, -1]]
        for index, i in enumerate(a):
            d.push([i, index])
            l1.append(d.adj())

        d2 = DDstack()
        d2.cmp = lambda a, b:a[0] > b[0]
        l2 = []
        d2.list=[ [-1, -1]]
        a.reverse()
        for index, i in enumerate(a):
            d2.push([i, index])
            l2.append(d2.adj())

        length = len(a)
        a.reverse()
        ans = 0
        for i in range(len(a)):
            a1 = l1[i]
            b = l2[length - i -1]
            left = None
            right = None
            if a1 == -1:
                left = 0
            else:
                left = i - a1[1] -1

            if b == -1:
                right =0
            else:
                right = length - b[1] -1 - i - 1
            # print(left, right)
            now = 1 + right + left
            # print(now, a)
            ans = max(ans, now * a[i])

        print(ans)
        return ans


class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0
        if matrix == []:
            return ans
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         matrix[i][j] = int(matrix[i][j])

        pre =[0 for i in range(len(matrix[0]))]
        s = Solution1()
        for i in range(0, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==1:
                    pre[j] += matrix[i][j]
                else:
                    pre[j] =0

            pre1 = sorted(pre)
            now = s.largestRectangleArea(pre1)
            # print(i,now)
            # print(pre)
            ans = max(ans, now)

        return ans

Solution.largestSubmatrix(None,[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1],[0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,1,1,1]])

