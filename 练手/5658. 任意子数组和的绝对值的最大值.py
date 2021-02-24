class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length  = len(nums)
        dp = [0 for i in range(length)]
        dp[0] = nums[0]
        for i in range(1, length):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        dp2 = [0 for i in range(length)]
        dp2[0] = nums[0]
        for i in range(1, length):
            dp2[i] = min(dp2[i - 1] + nums[i], nums[i])

        a = max(dp)
        b = abs(min(dp2))
        print(a, b)
        return max(a,b)
Solution.maxAbsoluteSum(None,[2,-5,1,-4,3,-2])

