class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        if high == low:
            if high %2 ==0:
                return 0
            else:
                return 1

        if high -low == 1:
            return 1

        ans  =0
        if low % 2 == 1:
            ans +=1
            low +=1
        if high %2  == 1:
            ans +=1
            high -=1

        ans += (high -low)/2


        # print(ans)
        return int(ans)


Solution.countOdds(None,5, 5)