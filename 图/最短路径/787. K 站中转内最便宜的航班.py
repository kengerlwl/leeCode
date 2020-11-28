class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        import collections
        import heapq
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')): continue
            if place == dst: return cost

            for nei, wt in graph[place].iteritems():
                newcost = cost + wt
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost

        return -1




Solution.findCheapestPrice(None,n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]],
src = 0, dst = 2, K = 1

)