
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
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        l1 = len(grid)
        l2 = len(grid[0])
        bq = BQSet()
        for i in range(l1):
            for j in range(l2):
                now = str(i) + '&' + str(j)
                bq.f[now] = now


        for i in range(l1):
            for j in range(l2):
                now = str(i) + '&' + str(j)
                if grid[i][j] == '1':
                    #分别向四个方向
                    for index in range(4):
                        x = i + dx[index]
                        y = j + dy[index]
                        new  = str(x) + '&' + str(y)
                        try:
                            # 同样就合并
                            if grid[x][y] == '1':
                                bq.Union(now, new)
                        except:
                            pass

        f = {}
        for i in bq.f:
            father = bq.getFather(i)
            x, y = i.split('&')
            x= int(x)
            y = int(y)
            # print(i,father)
            if father not  in f and grid[x][y] == '1':
                f[father] = True

        # print(len(f))
        return len(f)
s  = Solution()
s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])