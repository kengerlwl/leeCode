
# 第一种dp
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        dp = [0 for i  in  range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])   # DP[i]代表抢劫了第i个的时候最大值

        import heapq
        q = []
        for i in range(2, length):
            heapq.heappush(q, dp[i-2])
            t = heapq.nlargest(1,q)
            dp[i] = nums[i]  + t[0]

        # print(dp)
        return max(dp)


# 第二种dp

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length == 0 :
            return 0
        if length == 1:
            return nums[0]


        dp = [0 for i in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # DP[i]代表了前i个的时候最大值

        for i in range(2, length):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # print(dp)
        return max(dp)


Solution.rob(None,[1,3,1,3,100])