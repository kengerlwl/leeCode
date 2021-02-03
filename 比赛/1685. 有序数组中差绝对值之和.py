
import  math
class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        cur  = 0

        preSum = [0 for i in range(length+1)]
        for i in range(length):
            cur += nums[i]
            preSum[i+1] = cur
        # print(preSum)
        ans = []

        for index, i in enumerate(nums):
            leftSum = preSum[index]
            left  = index
            right = length - left -1
            rightSum = preSum[length] - preSum[index+1]
            # print(leftSum, rightSum)

            now = math.fabs(i* left - leftSum) + math.fabs(i* right - rightSum)
            print(now)
            ans.append(int(now))
        return ans






Solution.getSumAbsoluteDifferences(None,[2,3,5])