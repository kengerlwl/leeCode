class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        up =1
        for i in range(k, n +1):
            print(i)
            up *= i
        low =1
        for i in range(1, k+1):
            print(i)
            low *=i
        print(up, low)
        ans = up / low
        print(ans)



Solution.numberOfSets(None, 30, 7)