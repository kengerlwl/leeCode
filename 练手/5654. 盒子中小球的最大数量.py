class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        def cal(num):
            num = str(num)
            ans =0
            for i in num:
                ans += int(i)
            return ans
        f ={}
        ans = 0
        for i in range(lowLimit, highLimit+1):
            num = cal(i)
            if num in f:
                f[num]+=1
            else:
                f[num] =1
            ans = max(ans, f[num])

        return ans

Solution.countBalls(None,1,10)