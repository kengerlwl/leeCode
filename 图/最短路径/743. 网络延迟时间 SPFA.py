INF =float('inf')
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        arrived ={}   # 已经到的点
        for i in range(1, N + 1):
            arrived[i] = INF
        arrived[K] = 0


        adj ={} # 邻接表
        for i in range(1,N+1):
            adj[i] ={}

        for u, v, w in times:
            adj[u][v] =w


        q = [K]  # 优化队列
        vis ={}  # 是否正在队列里
        count = {}  # 统计在队列里出现多少次
        for i in range(1,N+1):
            vis[i] = False
            count[i] = 0
        vis[K] = True  # 代表在队列里面
        count[K] +=1
        while q:

            now = q.pop()
            vis[now] = False
            for i in adj[now]:
                to = i
                # 进行了松弛的点
                if arrived[to]> arrived[now] + adj[now][to]:
                    arrived[to] =  arrived[now] + adj[now][to]
                    if not vis[to]:
                        vis[to] = True
                        count[to] +=1
                        q.append(to)
                        if count[to] > N+1:
                            return False



        # print(arrived)
        if (max(arrived.values()) if len(arrived) == N else -1) == INF:
            return -1

        return max(arrived.values()) if len(arrived) == N else -1




a = Solution.networkDelayTime(None,[[1,2,1],[2,3,7],[1,3,4],[2,1,2]],
3,
2)
print(a)