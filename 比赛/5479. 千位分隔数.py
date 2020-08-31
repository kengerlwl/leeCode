class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """

        ans =""
        res= n % 1000
        n = n // 1000

        ans = str(res) + ans

        if n ==0:
            return ans
        if len(str(res)) == 2:
            ans  = "0" + ans
        elif len(str(res)) ==1:
            ans = "00" + ans

        while n !=0:

            res = n % 1000

            n = n // 1000
            ans = str(res) +"." + ans
            if n == 0:
                return ans

            if len(str(res)) == 2:
                ans  = "0" + ans
            elif len(str(res)) ==1:
                ans = "00" + ans


        return ans



ans = Solution.thousandSeparator(None, 7)
print(ans)