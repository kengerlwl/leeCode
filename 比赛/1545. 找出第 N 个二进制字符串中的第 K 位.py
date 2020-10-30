class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def reverse(a):
            if a == '0':
                return '1'
            else:
                return '0'

        import math
        def dg(n, k):

            if n == 1:
                return '0'

            mid = math.pow(2, n-1)
            if k == mid:
                return '1'
            elif k > mid:
                # print('r')
                return reverse(dg(n-1,mid - (k - mid)))
            elif k < mid:
                # print('l')
                return dg(n-1, k)


        ans = dg(n, k)
        print(ans)
        return ans

Solution.findKthBit(None,n = 4, k = 11)