class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        list = sorted(arr)

        length = len(list)
        dp = [0 for i in range(length)]
        start = 0
        if list[0] >=1:
            dp[0] =1



        for i in range(1,length):
            if list[i] <= dp[i-1] + 1:
                dp[i] = list[i]
            else:
                dp[i] = dp[i-1] + 1


        print(dp[length-1])
        return dp[length-1]


Solution.maximumElementAfterDecrementingAndRearranging(None,[73,98,9])


