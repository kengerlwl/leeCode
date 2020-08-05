class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return  nums[len(nums) // 2]


ans  = Solution.majorityElement(None,[2,2,1,1,1,2,2])
print(ans)