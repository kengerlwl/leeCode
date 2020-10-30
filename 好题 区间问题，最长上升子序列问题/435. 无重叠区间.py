
#  dp 简单思路
# class Solution(object):
#     def eraseOverlapIntervals(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: int
#         """
#         intervals = sorted(intervals)
#         print(intervals)
#
#         if len(intervals) ==0:
#             return 0
#
#
#         dp = [0 for  i in range(len(intervals))]
#         dp[0] = 1
#         length = len(intervals)
#         for i in range(1, length):
#             tmpM = 0
#             for j in range(0, i):
#                 if intervals[i][0] >= intervals[j][1]:
#                     tmpM = max(tmpM, dp[j]+1)
#             dp[i] = tmpM
#         ans = length - max(dp)
#         print(ans)
#         return ans
#


# 尝试优化 直接贪心

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if intervals == []: return 0
        ## 根据区间右端点排序
        intervals = sorted(intervals, key = lambda x: x[1])
        num = 0
        new_interval = intervals[0]     # 被选的最新区间
        for interval in intervals[1:]:
            if interval[0] < new_interval[1]:   # 如果重叠删除区间，删除数量+1
                num += 1
            else:   # 如果不重叠更新new_interval
                new_interval = interval
        num = len(intervals) - num
        print(num)

        return num


Solution.eraseOverlapIntervals(None,[[2, 4], [4, 6], [1, 7]])