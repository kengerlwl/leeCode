class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cur= 0
        ans  = -float('INF')
        for i in gain:
            cur+= i
            ans = max(ans, cur)
        return ans