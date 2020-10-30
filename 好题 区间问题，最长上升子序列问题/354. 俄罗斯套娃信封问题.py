class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n=len(envelopes)
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        dp=[1]*n
        res=1
        for i in range(1,n):
            for j in range(i):
                if envelopes[i][1]>envelopes[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
            res=max(res,dp[i])
        return res


Solution.maxEnvelopes(None,envelopes = [[5,4],[6,4],[6,7],[2,3]])