class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows = len(heights)
        columns = len(heights[0])

        #判断是不是正确的点
        def isRightPos(x, y):
            if x>= 0 and x < rows and y >=0 and y< columns:
                return True
            else:
                return False



        bias = [(1,0), (-1, 0), (0,1), (0,-1)]
        import math
        # 需要避免走重复路径，所以加入flag 进行判断， 因为每次传入不同的参数所以就相当于每次的路径
        f = False
        def dfs(x, y, flag, k):
            #print(x, y)
            flag[x][y] = False

            if x == rows-1 and y == columns-1:

                return True


            for bx, by in bias:
                #print(1)
                tmpx = x + bx
                tmpy = y + by

                if isRightPos(tmpx, tmpy) and flag[tmpx][tmpy]:
                    #print(2)
                    if math.fabs(heights[x][y] - heights[tmpx][tmpy]) <= k:
                        #print(3)
                        if dfs(tmpx, tmpy, flag, k):
                            return True
            return False

        flag = [[True for i in range(columns)] for i in range(rows)]
        # print(dfs(0,0,flag, 500000))








        l =0
        r = 1000000
        while l < r:
            flag = [[True for i in range(columns)] for i in range(rows)]

            mid = (l  + r ) //2
            f = dfs(0,0,flag, mid)
            # print(f)
            if f:
                r = mid
            else:
                l = mid+1
            # print(l,r)
        print(l)
        return l




Solution.minimumEffortPath(None,heights = [[1,2,3],[3,8,4],[5,3,5]])