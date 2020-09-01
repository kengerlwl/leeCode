class Solution(object):
    def winnerSquareGame(self, n):
        dp={}
        dp[0] = False
        dp[1] = True
        for i in range(2, n+1):
            dp[i] = False
            for j in range(1, n):
                tmp = j*j
                if tmp > i:
                    break

                if dp[i-tmp] == False:
                    dp[i] = True
                    break

        print(dp[n])
        return dp[n]





Solution.winnerSquareGame(None, 17)