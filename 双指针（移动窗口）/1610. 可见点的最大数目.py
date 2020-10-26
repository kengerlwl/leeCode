class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """

        # 要把等于的情况单独讨论
        import math
        pointAn = []
        count = 0
        tmp =[]
        for i in  range(len(points)):
            if points[i] == location:
                    count += 1
                    continue
            points[i][0] -= location[0]
            points[i][1] -= location[1]
            tmp.append(points[i])
        points = tmp
        for i in points:
            an = math.atan2(i[1], i[0])
            pointAn.append(an* 180 / math.pi)
        tmp =[]
        for i in pointAn:
            tmp.append(i)
            tmp.append(i + 360)
        pointAn = sorted(tmp)
        # print(pointAn)
        l= 0
        r =0
        ans  = 0
        while l < len(pointAn):
            if r >= len(pointAn):
                r = len(pointAn)-1
            while pointAn[r] - pointAn[l] <= angle:
                r+=1
                if r >= len(pointAn):
                    break
            # print(r -l)
            ans = max(ans, r-l)
            l+=1


        # print(ans +count)
        return ans + count







Solution.visiblePoints(None, [[2,1],[2,2],[3,4],[1,1]],
90,
[1,1])