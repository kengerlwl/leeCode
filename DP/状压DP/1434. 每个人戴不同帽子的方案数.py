class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        # 让人戴帽子的嵌套列表 -> 把帽子送人的字典
        d = {k: set() for k in range(1, 41)}
        n = len(hats)
        for i in range(n):
            for hat in hats[i]:
                d[hat].add(i)

        # 构造 dp table
        cols = 2 ** n
        # 第 0 行，没有可用帽子时，方案数为 0
        dp = [[0] * cols for i in range(41)]
        # 没有可用帽子，但又不用送帽子，方案数为 1
        dp[0][0] = 1

        for i in range(1,41):
            for j in range(cols):
                dp[i][j] += dp[i-1][j]

                for k in  d[i]:
                    if j & 1<<k !=0:
                        dp[i][j] += dp[i-1][j ^1<<k]

        return dp[-1][-1] % (10 ** 9 + 7)
