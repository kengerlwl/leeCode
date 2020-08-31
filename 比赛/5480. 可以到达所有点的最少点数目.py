class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ans =[]
        num ={}
        for i in range(n):
            num[i] = 0
        for i in edges:
            num[i[1]] +=1  # 计算入度
        for i in num:
            if num[i] ==0:
                ans.append(i)
        print(ans)
        return ans



Solution.findSmallestSetOfVertices(None, n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]])