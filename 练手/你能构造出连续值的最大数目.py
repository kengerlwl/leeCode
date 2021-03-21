import copy
class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins = sorted(coins)
        length = len(coins)
        dp = [[0, 0] for i in range(length+1)]
        def cal(l1, l2):
            # print()
            if l2[0] <= l1[1] +1:
                return [l1[0], l2[1]]
            else:
                return l2

        for i in range(1, length+1):
            now = coins[i-1]
            nowNums = dp[i-1]

            new = copy.deepcopy(nowNums)
            for j in range(len(new)):
                new[j] += now
            # print(i,nowNums, new)
            dp[i] = cal(nowNums, new)

        a  = dp[-1]
        ans =  a[1] -a[0]+1

        print(ans)
        return ans

Solution.getMaximumConsecutive(None,coins = [1,4,10,3,1])




