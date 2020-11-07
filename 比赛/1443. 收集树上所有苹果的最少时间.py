class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        adjList ={}
        for i in range(n):
            adjList[i] = []
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])

        # print(adjList)
        import  copy
        flag ={}
        for i in range(n):
            flag[i] = hasApple[i]

        count =[]
        # print(flag)
        ans ={}
        def dfs(n, road):

            if hasApple[n]:
                # print(n)
                # print(road)
                count.append(road)
                for i in range(len(road) - 1):
                    ans[(road[i], road[i+1])] = True


            # 获取n的邻接点
            for i in adjList[n]:

                tmpRoad = copy.deepcopy(road)
                tmpRoad.append(i)
                if i not in road:
                    # print(i)
                    dfs(i, tmpRoad)
        r = [0]
        dfs(0,r)
        # print(ans)
        # print(len(ans))
        # #
        # #
        # print(count)
        #
        return len(ans) * 2


Solution.minTime(None,4,
[[0,2],[0,3],[1,2]],
[False,True,False,False])