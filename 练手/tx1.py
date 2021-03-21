class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        employee = {}
        for i in range(n):
            father = manager[i]
            if father in employee:
                employee[father].append(i)
            else:
                employee[father] = [i]

        # print(employee)

        queue = [[headID, informTime[headID]]]
        ans = 0
        while queue:
            now , time = queue.pop()
            print(now, time)
            if now not in employee:
                ans = max(time, ans)
                continue
            for i in employee[now]:
                queue.append([i, time + informTime[i]])


        print(ans)
        return ans


Solution.numOfMinutes(None,n = 1, headID = 0, manager = [-1], informTime = [0])

