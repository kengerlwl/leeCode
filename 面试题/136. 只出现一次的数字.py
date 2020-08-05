class Solution(object):

    # 排序以后就直接ak
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # print(nums)
        if len(nums) ==1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]

        for i in range(1, len(nums)-2):



            if nums[i] == nums[i-1] or nums[i] == nums[i+1]:
                pass
            else:
                return nums[i]

        return nums[-1]
