class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        import copy
        # cardPoints = []
        zhen = copy.deepcopy(cardPoints)
        cardPoints.reverse()
        fan = cardPoints

        preSumZ = [0]
        cur = 0
        for i in zhen:
            cur+=i
            preSumZ.append(cur)


        preSumF = [0]
        cur = 0
        for i in fan:
            cur+=i
            preSumF.append(cur)

        ans = 0
        # print(preSumZ)
        # print(preSumF)
        for i in range(k+1):
            left = preSumZ[i]
            right  = preSumF[k-i]
            tmp = left+ right
            # print(tmp)
            ans = max(ans,tmp)

        return ans
Solution.maxScore(None,[100,40,17,9,73,75],
3)