class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum = [0]
        cur =0
        for i in nums:
            cur+=i
            sum.append(cur)

        ans =0
        sumDict ={}
        sumDict[0] =1
        for i in range(len(nums)):
            target = sum[i+1] -k

            if target in sumDict:
                ans+= sumDict[target]



            if sum[i+1] in sumDict:
                sumDict[sum[i + 1]]+=1
            else:
                sumDict[sum[i + 1]]=1
        print(ans)
        return ans

Solution.subarraySum(None,nums = [1,1,1], k = 2)
