class Solution(object):
    def longestSubarray(self, nums, limit):
        if not nums:
            return 0
        curr_max = nums[0] # 当子数组下最大值 这里初始化为第一个数
        curr_min = nums[0] # 当子数组下最大值 这里初始化为第一个数
        sub_nums = [] # 以数组作为窗口滑动
        for num in nums:
            if abs(num - curr_max) <=  limit and abs(num - curr_min) <=  limit and abs(curr_max - curr_min) <= limit:
                curr_max = max(num,curr_max)
                curr_min = min(num,curr_min)
                sub_nums.append(num)
            else:
                sub_nums.append(num)
                sub_nums.pop(0)
                curr_max = max(sub_nums) # 当子数组最大值
                curr_min = min(sub_nums) # 当前子数组最小值
        return  len(sub_nums)





Solution.longestSubarray(None,nums = [8,2,4,7], limit = 4)