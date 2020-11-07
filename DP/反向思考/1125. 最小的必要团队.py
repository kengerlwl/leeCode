#
#
# S表示一个二进制集合.SS中第ii位是11表示该集合包含标号是ii的技能
#
# 令dp[S]dp[S]表示要获得集合SS表示的技能的最小花费.也就是最少需要选多少人
#
# 假设技能个数是nn,那么要求的答案就是dp[(1 << n)-1]dp[(1<<n)−1]
#
# 对于状态转移方程:
#
# 假设当前第ii个人的技能集合是nownow.我们就拿当前的技能集合
#
# nownow去更新每一个dp[now|j], 0 <= j < (1 << n)dp[now∣j],0<=j<(1<<n)的值.
#
# 因为要记录最后所选的答案.所以拿一个teamteam数组维护一下
#
# 时间复杂度O(m*2^n)O(m∗2
# n
#  ).mm是人的个数,nn是技能个数


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 为skills建立字典
        n = len(req_skills)
        d = dict()
        for i in range(n):
            d[req_skills[i]] = i
        # 所有状态
        dp = [list(range(len(people))) for _ in range(1 << n)]
        dp[0] = []
        # 遍历所有人
        for i in range(len(people)):
            # 求这个人的技能
            skill = 0
            for s in people[i]:
                skill |= (1 << d[s])
            for k, v in enumerate(dp):
                # 把这个人加入进来以后的团队技能
                new_skills = k | skill
                # 如果团队技能因此而增加 并且增加后的人数比新技能原来的人数少 则更新答案
                if new_skills != k and len(dp[new_skills]) > len(v) + 1:
                    dp[new_skills] = v + [i]
        return dp[(1 << n) - 1]

