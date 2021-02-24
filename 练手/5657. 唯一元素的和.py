class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f  ={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i] =1

        ans =0
        # print(f)
        for i in f:
            if f[i] == 1:
                ans+= i

        print(ans)
        return ans

Solution.sumOfUnique(None,[1,2,3,2])