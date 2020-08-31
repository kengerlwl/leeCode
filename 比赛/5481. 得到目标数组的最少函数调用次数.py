class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans =0

        def check(num):

            for i in num:
                if i !=0:
                    return False
            return True



        while not check(nums):
            tmp = True
            for ix in range(len(nums)):
                if nums[ix] % 2!=0:
                    tmp = False
                    nums[ix] -= 1
                    ans +=1
            if tmp: # 全部是偶数
                for ix in range(len(nums)):
                    nums[ix] = nums[ix] //2
                ans +=1
            # print(nums)
            # print(ans)
        return ans






Solution.minOperations(None, nums = [4,2,5])