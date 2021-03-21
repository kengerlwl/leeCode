class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length  = len(cost)
        inf = float('INF')
        dp = [inf for i in range(length+1)]
        dp[0] = 0
        dp[1] = 0

        for i in range(2,length+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        print(dp[length])
        return dp[length]




Solution.minCostClimbingStairs(None,cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1])