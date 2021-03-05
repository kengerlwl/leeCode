
#暴力循环， 失败，超时了
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         def judgeH(s, l, r):
#             mid = (l +r) /2
#             # print(s[r])
#             while(l < r):
#                 if s[l] != s[r]:
#                     return False
#                 l +=1
#                 r -=1
#             return True
#
#
#         l= len(s)
#         max = 1
#         Fl =0
#         FR =0
#         for ix, i in enumerate(s):
#             for j in range(ix, l):
#                 if judgeH(s, ix, j):
#                     tmp  = j -ix +1
#                     #print(ix, j)
#                     if tmp > max:
#                         max = tmp
#                         Fl =ix
#                         FR = j
#                         #print(s[Fl:FR+1])
#
#         #print()
#         return s[Fl:FR+1]


# 试试dp,动态规划不断变长
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        print(dp)

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]





Solution.longestPalindrome(None, "cbbd")