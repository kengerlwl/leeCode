


# 好题 就是KMP的推导过程的一环， next数组
class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """

        dp = [0 for i in range(len(s))]
        curLength =0
        for i in range(1, len(s)):

            # 找到满足的最大的子前缀
            while curLength > 0 and s[i] != s[curLength]:
                curLength = dp[curLength-1]

            # 判断子前缀是否相等
            if s[i] ==s[curLength]:
                curLength+=1
            dp[i] = curLength

        print(dp[-1])
        return dp[-1]


Solution.longestPrefix(None,  "level")