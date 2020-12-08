class Solution(object):
    def kConcatenationMaxSum1(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        sumOfA = sum(arr)
        if k>=3:
            ans = 0

            if sumOfA >0:
                ans += (k-2) *sumOfA
            # b =1
            import copy
            arr = arr + copy.deepcopy(arr)
            dp = [0 for i in range(len(arr))]
            dp[0] = arr[0]
            for i in range(1, len(arr)):
                dp[i] = max(dp[i - 1] + arr[i], arr[i])

            # print(dp)
            return max(dp) + ans


        elif k ==2:
            import copy
            arr = arr + copy.deepcopy(arr)
            dp = [0 for i in range(len(arr))]
            dp[0] = arr[0]
            for i in range(1, len(arr)):
                dp[i] = max(dp[i - 1] + arr[i], arr[i])

            # print(dp)
            return max(dp)
        elif k ==1:
            dp = [0 for i in range(len(arr))]
            dp[0] = arr[0]
            for i in range(1, len(arr)):
                dp[i] = max(dp[i - 1] + arr[i], arr[i])

            # print(dp)
            return max(dp)
    def kConcatenationMaxSum(self, arr, k):
        a = self.kConcatenationMaxSum1(arr, k)
        return max(a , 0)%(10**9 +7)
t  =Solution()
a = Solution.kConcatenationMaxSum(t,[-1,-2],
7)
print(a)