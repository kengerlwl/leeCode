class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        start = 0
        end = 1
        nowTotal = 0
        minLen = 9999999999

        preSum = [0 for _ in range(n+1)]
        # 计算前缀和
        for i in range(1, n+1):
            preSum[i] = preSum[i-1] + nums[i-1]

        # 当前窗口的和小于target，end右移
        # 当前窗口的和大于target，start右移
        while end <= n:
            nowTotal = preSum[end] - preSum[start]
            # print(start, end)
            # print(nowTotal)
            if nowTotal < target:
                end += 1
            else:
                # print('nowTotal:', nowTotal)
                minLen = min(minLen, end-start)
                start += 1
            
        if minLen == 9999999999:
            return 0
        return minLen


target =15
nums = [1,2,3,4,5]
s = Solution()
print(s.minSubArrayLen(target, nums))