class Solution(object):
    def dicesProbability(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp = {}
        for i in range(n):
            dp[i] = {}


        for i in range(1,6+1):
            dp[0][i] = 1/6

        for i in range(1, n):
            maxN = 6 * (i+1)
            print(maxN)
            for j in range(i+1, maxN+1):
                dp[i][j] = 0

                for k in range(1,7):
                    try:
                        dp[i][j] += dp[i-1][j-k]
                    except Exception:
                        pass
                dp[i][j] /=6


        num = list(dp[n-1].values())
        for i in range(len(num)):
            num[i] = round(num[i], 5)
            print(num[i])
        print(num)
        return num






Solution.dicesProbability(None, 1)