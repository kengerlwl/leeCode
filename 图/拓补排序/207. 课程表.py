class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 计算入度
        ind = {}
        adj ={} # 邻接表
        vis = {}
        for i in range(numCourses):
            adj[i]=[]
            ind[i] = 0
            vis[i] = False

        for u,v in prerequisites:
            ind[v] +=1
            adj[u].append(v)


        queue = []
        for i in ind:
            if ind[i] ==0:
                queue.append(i)


        count = 0
        while queue:
            a = queue.pop()  # 删除入度为0 的点
            vis[a] = True
            count +=1
            for i in adj[a]: # 访问邻接点 , 减小入度
                ind[i] -=1
                if ind[i] == 0 and not vis[i]:
                    queue.append(i)

        print(count)
        if count == numCourses:
            return True
        else:
            return False

Solution.canFinish(None, 2, [[1,0]] )




