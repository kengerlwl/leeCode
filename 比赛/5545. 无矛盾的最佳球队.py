class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        peo={}
        for i in range(len(scores)):
            peo[i] = [ages[i],scores[i]]

        peo = sorted(peo.values())

        print(peo)

        dp= [[0, 0] for i in range(len(scores) +1)]

        for i in range(len(scores)):
            m =0
            for j in range(0, i+1):

                if dp[j][1] <= peo[i][1]:
                    m = max(dp[j][0], m)


            dp[i +1][0]  = m + peo[i][1]
            dp[i +1][1] =peo[i][1]


        m = 0
        for i in dp:
            m= max(i[0], m)

        return m






Solution.bestTeamScore(None,[9,2,8,8,2],
[4,1,3,3,5]
                       )

#
# l = 0
# r = 0
# ans = 0
# tmpM = 0
# pre = peo[l]
# while l < len(peo):
#
#
#
#     if peo[r][1] >= pre[1] or peo[r][0] == pre[0] :
#         tmpM+= peo[r][1]
#         pre = peo[r]
#         ans = max(tmpM,ans ) # 如果更大就更新
#
#
#     r +=1
#     if r == len(peo):
#         l += 1
#         r = l
#         tmpM =0
#         if l == len(peo):
#             break
#         pre = peo[l]
#
#
# print(ans)
# return ans