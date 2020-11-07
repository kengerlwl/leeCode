class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        a = []
        for i in buildings:
            a.append([i[0], -i[2]])
            a.append([i[1], i[2]])
        a.sort(key=lambda x: (x[0], -x[1]))
        i = 0

        last = [0, 0]
        d = {}
        heap = [0]
        res = [[0, 0]]
        for j in a:
            if j[1] < 0:
                heapq.heappush(heap, j[1])  # heapq是小堆，所以这里把负值push进去
            else:
                d[j[1]] = 0

            while heap and -heap[0] in d:
                t = -heap[0]
                heapq.heappop(heap)
                d.pop(t)

            maxH = -heap[0]

            if last[1] != maxH:
                last = [j[0], maxH]
                if last[0] == res[-1][0]:
                    res.pop()
                if not res:
                    res.append(last)
                elif last[1] != res[-1][1]:
                    res.append(last)

        if res[0] == [0, 0]:
            return res[1:]
        return res

Solution.getSkyline(None,[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
