class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        max =arr[0]
        len =0
        f = True
        for i in arr:
            if f:
                f = False
                continue
            if max > i:
                len +=1
            else:
                len =1
                max = i
            if len ==k:
                return max
        return max



ans  = Solution.getWinner(None, [3,2,1]
,10)
print(ans)