class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """

        nums = {}

        nums[0] =0
        nums[1] =1
        count =2
        ans  =1
        if n == 2:
            return 1
        if n ==1:
            return 1
        if  n ==0:
            return 0
        for i in range(1, n):
            even = i *2
            odd = even +1

            nums[even] = nums[i]
            count +=1

            if count == (n+1):
                break


            nums[odd] = nums[i] + nums[i+1]
            if nums[odd] > ans:
                ans = nums[odd]
            count +=1
            if count == (n+1):
                break
        print(nums)
        ans = max(nums.values())
        return ans

Solution.getMaximumGenerated(None, 3)
