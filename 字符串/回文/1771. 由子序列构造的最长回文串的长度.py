class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        n1 = len(word1)
        # 依然是动态规划 dp[i][j]表示word[i:j+1]范围内最长回文子串的长度
        # dp[i][j] = dp[i+1][j-1] + 2 if word[i]==word[j]
        # dp[i][j] = max(dp[i+1][j], dp[i][j-1]) if word[i]!=word[j]
        n = len(word)
        dp = [[0]*n for _ in range(n)]
        ans = 0
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1):
            if word[i]==word[i+1]:
                dp[i][i+1] = 2
                if i==n1-1:
                    ans = 2
            else:
                dp[i][i+1] = 1
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                if word[i]==word[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                    if i<n1 and j>=n1:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return ans