# class Solution(object):
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         l1 = len(word1)
#         l2 = len(word2)
#         dp =[ [0 for i in range(l2)] for i in range(l1) ]
#
#         c =0
#         f=True
#         for i in range(l1):
#             if word2[0] in word1[0:i+1] and f:
#                 dp[i][0] =c
#                 f = False
#             else:
#                 c+=1
#                 dp[i][0] =c
#
#
#         c =0
#         f=True
#         for i in range(l2):
#             if word1[0] in word2[0:i+1] and f:
#                 dp[0][i] =c
#                 f = False
#             else:
#                 c+=1
#                 dp[0][i] =c
#
#
#
#         for i in range(1, l1):
#             for j in  range(1, l2):
#                 if word1[i] == word2[j]:
#                     dp[i][j] = dp[i-1][j-1]
#                 else:
#                     dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) +1
#
#         print(dp[l1-1][l2-1])
#
#         return dp[l1-1][l2-1]
#
#
#
#
#         # if word2[0] == word1[0]:
#         #     dp[1].append(dp[0][0] +1)
#         # else:
#         #     if word2[0] == word1[1]:
#         #         dp[1].append(1)
#         #     else:
#         #         dp[1].append(2)
#         # print(dp)
#

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)


        print(D[n][m])

        return D[n][m]






Solution.minDistance(None, word1 = "", word2 = "")