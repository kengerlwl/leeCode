# 有点难理解，还没彻底吃透

class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        BIG = 2 ** 30
        dp = [[[BIG] * 26 for x in range(26)] for y in range(n)]
        for i in range(26):
            dp[0][i][ord(word[0]) - 65] = 0
            dp[0][ord(word[0]) - 65][i] = 0

        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(1, n):
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            d = getDistance(prev, cur)
            for j in range(26):
                dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][prev][j] + d)
                dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][prev] + d)
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][k][j] + d0)
                        dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][k] + d0)

        ans = min(min(dp[n - 1][x]) for x in range(26))
        return ans

