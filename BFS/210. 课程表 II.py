# class Solution(object):
#     def findOrder(self, numCourses, prerequisites):
#         """
#         :type numCourses: int 课程门数
#         :type prerequisites: List[List[int]] 课程与课程之间的关系
#         :rtype: bool
#         """
#         # 课程的长度
#         clen = len(prerequisites)
#         if clen == 0:
#             # 没有课程，当然可以完成课程的学习
#             return [i for i in range(numCourses)]
#         # 入度数组，一开始全部为 0
#         in_degrees = [0 for _ in range(numCourses)]
#         # 邻接表
#         adj = [set() for _ in range(numCourses)]
#         # 想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#         # 1 -> 0，这里要注意：不要弄反了
#         for second, first in prerequisites:
#             in_degrees[second] += 1
#             adj[first].add(second)
#
#         # print("in_degrees", in_degrees)
#         # 首先遍历一遍，把所有入度为 0 的结点加入队列
#         res = []
#         queue = []
#         for i in range(numCourses):
#             if in_degrees[i] == 0:
#                 queue.append(i)
#
#         while queue:
#             top = queue.pop(0)
#             res.append(top)
#
#             for successor in adj[top]:
#                 in_degrees[successor] -= 1
#                 if in_degrees[successor] == 0:
#                     queue.append(successor)
#         if len(res) != numCourses:
#             return []
#         return res



class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int 课程门数
        :type prerequisites: List[List[int]] 课程与课程之间的关系
        :rtype: bool
        """
        # 课程的长度
        clen = len(prerequisites)
        if clen == 0:
            # 没有课程，当然可以完成课程的学习
            return [i for i in range(numCourses)]
        # 入度数组，一开始全部为 0
        in_degrees = [0 for _ in range(numCourses)]
        # 邻接
        adj= {}
        for i in range(numCourses):
            adj[i] = set()

        # 初始化表
        for second, first in prerequisites:
            in_degrees[second] += 1
            adj[first].add(second)

        queue = []

        # 入度为0入队列
        for i in range(numCourses):
            if in_degrees[i] ==0:
                queue.append(i)
        res =[]
        while(len(queue) !=0):
            top = queue.pop()
            res.append(top)
            for i in adj[top]:
                in_degrees[i] -=1
                if in_degrees[i] ==0:
                    queue.append(i)
        if len(res) != numCourses:
            return []
        else:
            return res



        # print(adj, in_degrees)

        

Solution.findOrder(None,4, [[1,0],[2,0],[3,1],[3,2]])