class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        charSet ={}
        for i in target:
            charSet[i] = True
        ans =[]
        maxV = max(target)
        for i in range(1,n+1):
            if i > maxV:
                break
            if i in charSet:
                ans.append('Push')
            else:
                ans.append('Push')
                ans.append('Pop')

        print(ans)
        return ans
Solution.buildArray(None,[1,2],
4)