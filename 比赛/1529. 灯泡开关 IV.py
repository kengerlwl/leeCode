class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        ans =0
        tmp = target[0]
        f = True
        for i in target:
            if f:
                f = False
                continue
            print(i)
            if tmp == i:
                continue

Solution.minFlips(None, '00001')