
import collections
INF =float('inf')
import heapq
class Dijkstra(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """


        adj ={} # 邻接表
        for i in range(1,N+1):
            adj[i] ={}



        for u, v, w in times:
            adj[u][v] =w
            adj[v][u] = w



        def dijkstra(adj, K): #K是出发的点， 这里默认到达所有点
            arrived ={}   # 已经到的点
            pq = [(0, K)]# 存储需要到的点的最短值
            while pq:
                d, node = heapq.heappop(pq)
                if node in arrived: # 如果已经到达，
                    continue
                arrived[node] = d
                # print(node)
                for nei in adj[node]:
                    if nei not in arrived:
                        heapq.heappush(pq, (d + adj[node][nei], nei))

            return arrived


        return dijkstra(adj, K),adj


class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """


        d= Dijkstra()
        arrive, adj = d.networkDelayTime(edges, n, n)
        # arrive ={}
        # for i in range(1, n+1):
        #     arrive[i] = []
        start =1
        queue = []
        note = {}
        m = 10**9 +7
        def get(start):

            if start == n:
                return 1


            if start in note:
                return note[start]
            ans =0
            for i in adj[start]:
                if arrive[start] > arrive[i]:
                    ans += get(i)



            note[start] = ans
            return ans % m

        return get(start)



a = Solution.countRestrictedPaths(None,n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]])
print(a)