import copy
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        list =copy.deepcopy(A)
        for ix,i in enumerate(A):
            list.insert(ix, i)
            # list.insert(len(list), i)
        print(list)
        length = len(list)
        max = -10000
        for i, con in enumerate(list):
            j =i
            sum = 0

            while(j -i <= (length/2-1) and j < length-1):

                sum += list[j]

                if(sum > max):
                    max = sum

                j= j +1

        return max

ans  = Solution.maxSubarraySumCircular(None,[5,-3,5])
print(ans)