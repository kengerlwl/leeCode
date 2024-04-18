class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """


        betterNode = {}
        inDegree =[0 for i in range(n)]
        vis = {}
        for u, v in edges:
            betterNode[v] = u
            inDegree[v] +=1
            
        ans =[]
        for i in range(n):
            if inDegree[i] == 0:
                ans.append(i)
            
        
        ret = ans[0] if len(ans) == 1 else -1
        return ret
