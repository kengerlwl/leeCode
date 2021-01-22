# # Dynamic programming.
# class Solution:
#     def lengthOfLIS(self, nums):
#         if not nums: return 0
#         dp = [1] * len(nums)  # 包涵第i个元素时的max
#
#
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)



# 尝试优化
# Dynamic programming + Dichotomy.
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0  # tail 是用来维护目前某个长度的的最小返回值的队列，而且肯定是单调递增的。可以反证。
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1

        print(tails, res)
        return res

# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/


Solution.lengthOfLIS(None,[1,2,3,4,5,2,4])