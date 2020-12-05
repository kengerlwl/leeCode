from sortedcontainers import SortedList


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = SortedList(num << 1 if num & 1 else num for num in nums)

        ans = nums[-1] - nums[0]
        while not nums[-1] & 1:
            nums.add(nums.pop() >> 1)
            ans = min(ans, nums[-1] - nums[0])

        return ans



Solution.minimumDeviation(None,nums =[4,1,5,20,3])
