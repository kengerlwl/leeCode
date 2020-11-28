
# 2、Floyd算法可以解决多源最短路径；
# k 前k个点代表在前k个的前提下的最短路径

import collections
INF =float('inf')
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """


        adj ={} # 邻接表
        # 初始化邻接表
        for i in range(1,N+1):
            adj[i]={}
            for j in range(1,N+1):
                adj[i][j]  = INF
                if i ==j:
                    adj[i][j] = 0

        for u, v, w in times:
            adj[u][v] =w

        def floyd(adj):
            for k in range(1, N+1):
                for i in range(1, N + 1):
                    for j in range(1, N + 1):
                        adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])


            return adj

        adj = floyd(adj)


        if max(adj[K].values()) == INF:
            return -1

        return max(adj[K].values())


a = Solution.networkDelayTime(None,times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2)
print(a)