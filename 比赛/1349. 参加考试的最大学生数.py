from functools import reduce
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0]),
        dp = [[0]*(1 << n) for _ in range(m+1)]  # 状态数组 dp
        a = [reduce(lambda x,y:x|1<<y,[0]+[j for j in range(n) if seats[i][j]=='#'])  for i in range(m)] # 将 # 设为 1，当遇到 . 时与运算结果为 0，表示可以坐人
        # print(a)
        for row in range(m)[::-1]: # 倒着遍历
            for j in range(1 << n):
                if not j & j<<1 and not j&j>>1 and not j & a[row]: # j & a[row]代表该位置可以坐人，j & j<<1 and not j&j>>1 表示该位置左右没人可以坐的
                    for k in range(1 << n):
                        if not j&k<<1 and not j&k>>1: # j状态的左上和右上没有人
                            dp[row][j] = max(dp[row][j], dp[row+1][k] + bin(j).count('1'))
        # print(dp)
        return max(dp[0])