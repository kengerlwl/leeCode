class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        bias = [(1,0), (-1, 0), (0,1), (0,-1)]
        import math
        # 需要避免走重复路径，所以加入flag 进行判断， 因为每次传入不同的参数所以就相当于每次的路径
        f = False
        rows = len(grid)
        columns = len(grid[0])

        #判断是不是正确的点
        def isRightPos(x, y):
            if x>= 0 and x < rows and y >=0 and y< columns:
                return True
            else:
                return False


        def dfs(x, y, flag, k):
            #print(x, y)
            flag[x][y] = False

            if grid[x][y] > k:
                return False

            if x == rows-1 and y == columns-1:

                return True


            for bx, by in bias:
                #print(1)
                tmpx = x + bx
                tmpy = y + by

                if isRightPos(tmpx, tmpy) and flag[tmpx][tmpy]:
                    #print(2)
                    if math.fabs(grid[tmpx][tmpy]) <= k:
                        #print(3)
                        if dfs(tmpx, tmpy, flag, k):
                            return True
            return False



        l = 0
        r = 2500
        import math
        while l < r:
            mid = math.floor(( l + r) /2) # 向下取整
            flag = [[True for i in range(columns)] for i in range(rows)]

            if dfs(0, 0, flag, mid):
                r = mid
            else:
                l = mid + 1
        print(r, l)
        return int(r)


Solution.swimInWater(None,[[3,2],[0,1]])