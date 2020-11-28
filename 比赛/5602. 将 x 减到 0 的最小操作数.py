class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        preSum =[]
        curSum =0
        for i in nums:
            curSum+=i
            preSum.append(curSum)

        target = preSum[len(preSum) -1] - x
        # print(preSum)

        hashSet ={}
        hashSet[0] =-1

        if curSum == x:
            return len(nums)

        ans =float('-INF')
        for i in range(len(nums)):
            tmpT= preSum[i] - target
            print(tmpT,hashSet)
            print('\n')


            if tmpT in hashSet:
                ans = max(ans, i - hashSet[tmpT])
            else:
                hashSet[preSum[i]] = i


        print(ans)
        print(len(nums) - ans)

        if ans == float('-INF'):
            return -1

        return len(nums) - ans


Solution.minOperations(None,[8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309],
134365)


