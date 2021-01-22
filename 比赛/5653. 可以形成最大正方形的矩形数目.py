class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        ans = 1
        nowCount = 1
        nowMax = min(rectangles[0])

        for i in range(1, len(rectangles)):
            a, b = rectangles[i]
            tmp = min(a, b)

            if tmp > nowMax:
                nowCount =1
                nowMax = tmp
            elif tmp == nowMax:
                nowCount+=1
            ans = max(ans, nowCount)


        print(nowCount)
        return nowCount


Solution.countGoodRectangles(None,[[3,12],[3,9],[8,5]])