INF =float('inf')
class Solution(object):
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



        # 这是核心
        for k in range(1, N+1):
            for i in times: # 遍历所有边

                arrived[i[1]] = min(arrived[i[1]], arrived[i[0]] + i[2])





        # print(arrived)
        if (max(arrived.values()) if len(arrived) == N else -1) == INF:
            return -1

        return max(arrived.values()) if len(arrived) == N else -1




a = Solution.networkDelayTime(None,[[1,2,1],[2,3,7],[1,3,4],[2,1,2]],
3,
2)
print(a)