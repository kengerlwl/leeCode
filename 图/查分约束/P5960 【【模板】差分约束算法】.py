# 总结一下，SPFA是如何做到“只更新可能更新的点”的？
#
# 只让当前点能到达的点入队
# 如果一个点已经在队列里，便不重复入队
# 如果一条边未被更新，那么它的终点不入队


INF =float('inf')
class SPFA(object):
    def networkDelayTime(self, edges, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        times =edges
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
                        if count[to] > N+1:  #  //判断负环，
                            return False


        return arrived







n, m =input().split(' ')
n =int(n)
m= int(m)


edges =[]
for i in range(m):
    s= input().split(' ')
    edges.append([int(s[1]),int(s[0]),int(s[2])  ] )


# print(edges)
for i in range(n):
    edges.append([n+1, i+1, 0])

spfa = SPFA()

a= spfa.networkDelayTime(edges, n+1, n+1)

if not a:
    print('NO')
else:
    # print(a)
    flag =False
    for i in range(1, n+1):
        if a[i] == INF:
            flag =True

    if flag:
        print('NO')
    for i in range(1, n+1):
        print(a[i], end=' ')
