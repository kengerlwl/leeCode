class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        odd =0
        even =0
        result =0
        for i in arr:
            if i %2 ==0:
                even +=1
            else:
                tmp = even
                even = odd
                odd = tmp +1

            result += odd

        # print(result)
        ans = result % (1000000000 +7)

        # print(ans)
        return ans



Solution.numOfSubarrays(None,  [64,69,7,78,31,83,47,84,47,6,67])