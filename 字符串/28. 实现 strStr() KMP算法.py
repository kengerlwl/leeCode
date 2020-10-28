
# 学习自  https://leetcode-cn.com/problems/implement-strstr/solution/kmp-suan-fa-xiang-jie-by-labuladong/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        dp = None
        def kmp(s):  # 一个状态机
            length = len(s)
            dp = [[0 for i in range(256)] for i in range(length)]
            dp[0][s[0]] = 1 #第一个状态
            X =0  # 影子状态

            for i in range(1,length):
                for j in range(256):
                    dp[i][j] = dp[X][j]
                dp[i][s[i]] = j+1
                X = dp[X][s[j]]

        kmp(needle)
        def search(txt):
            N = len(txt)
            M = len(needle)
            j =0
            for i in range(N):
                j = dp[j][txt[i]]
                if j ==M:
                    return i- M +1

            return -1

        print(search(haystack))
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle == '': return 0
#         n = len(needle)
#         m = len(haystack)
#         j = 0
#         pnext = self.getnext(needle)
#
#         for i in range(m):
#             while j > 0 and needle[j] != haystack[i]:
#                 j = pnext[j]
#             if needle[j] == haystack[i]:
#                 j += 1
#                 if j == n:
#                     return i - n + 1
#         return -1
#
#     def getnext(self, s):
#         n = len(s)
#         pnext = [0, 0]  # 多一个前导0是为了方便后续指针跳跃，避免死循环
#         j = 0
#         for i in range(1, n):
#             while j > 0 and s[i] != s[j]:
#                 j = pnext[j]  # 指针跳跃
#             if s[j] == s[i]:
#                 j += 1
#             pnext.append(j)
#         return pnext




Solution.strStr(None,haystack = "hello", needle = "ll")


