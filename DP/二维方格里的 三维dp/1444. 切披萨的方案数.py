class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        # dp[m][n][k]
        dp = [[[0] * k for j in range(n)] for i in range(m)]

        # nums[i][j]: how many apples in pizza[i:][j:]


        #提前将部分需要用得数据计算好
        nums = [[False] * n for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n - 1, -1, -1):
                hasApple = pizza[i][j] == "A"
                if i == m - 1 and j == n - 1:
                    nums[i][j] = hasApple
                elif i == m - 1:
                    nums[i][j] =  hasApple + nums[i][j + 1]
                elif j == n - 1:
                    nums[i][j] =  hasApple + nums[i + 1][j]
                else:
                    nums[i][j] =  hasApple + nums[i + 1][j] + nums[i][j + 1] - nums[i + 1][j + 1]



        # 进行状态转移
        # dp[i][j][p] = sum(dp[x][j][p] for x in [i+1,m-1]) + sum(dp[i][y][p] for y in [j+1, n-1])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if nums[i][j]:
                    dp[i][j][0] = 1
                for p in range(1, k):
                    for x in range(i+1, m):
                        if nums[i][j] - nums[x][j]:
                            dp[i][j][p] += dp[x][j][p-1] % mod
                    for y in range(j+1, n):
                        if nums[i][j] - nums[i][y]:
                            dp[i][j][p] += dp[i][y][p-1] % mod
        return dp[0][0][k-1] % mod



# 讲解得很不错
# 作者：coldme-2
# 链接：https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza/solution/dong-tai-gui-hua-by-coldme-2-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。