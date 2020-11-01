class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x =[]
        hashSet ={}
        for i in points:
            x.append(i[0])
            tmpx = i[0]
            hashSet[tmpx] =True

        x = sorted(hashSet)
        print(x)
        maxV =0
        for i in range(len(x)-1):
            maxV = max(maxV, x[i+1] -x[i])
        print(maxV)
        return maxV



Solution.maxWidthOfVerticalArea(None, [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]])