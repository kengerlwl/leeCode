class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def cal(n):
            left = n % 10
            n = n // 10
            ans = []
            while left != 0 or n != 0:
                ans.append(left)
                left = n % 10
                n = n  // 10
                # print(left, n)
            ans
            S = 0
            # print(ans)
            for i in ans:
                S += i* i
            return S

        count = 1
        # print(cal(100))
        # return 1
        note  ={}
        while count < 10000:
            if n  in note:
                return False


            note[n] = True
            # print(n)
            if n == 1:
                return True
            else:
                n = cal(n)

        return False




a = Solution.isHappy(None,2)
print(a)