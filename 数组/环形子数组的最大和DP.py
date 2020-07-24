import copy
class Solution(object):

    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def kadane(nums):
            result = cur = float('-inf')
            for num in nums:
                #包含当前得num得子数组得最大情况
                cur = max(cur, 0) + num
                result = max(result, cur)
            return result

        max_A = max(A)
        if max_A < 0:
            return max_A
        result1 = kadane(A)
        result2 = sum(A) + kadane([-num for num in A])
        return max(result1, result2)

ans  = Solution.maxSubarraySumCircular(None,[1,-2,3,-2])
print(ans)