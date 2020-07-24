class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [-1000] * (n+1)
        dpi = [-1000] * (n+1)

        def getIMax(i):
            # tmpMax = -100000000
            # sum = 0
            # while(i >= 0):
            #     sum += nums[i]
            #     if(sum > tmpMax):
            #         tmpMax = sum
            #     i = i -1
            dpi[i] = max(dpi[i-1] + nums[i],nums[i] )


            return dpi[i]


        for index, i in enumerate(nums):
            j = index +1
            maxi = getIMax(index)
            # print(maxi)
            dp[j] = max(dp[j-1],maxi)

        print(dp)
        return dp[n]

Solution.maxSubArray(None,  [-2,1,-3,4,-1,2,1,-5,4])