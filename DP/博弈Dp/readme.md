# Leetcode T877 石子游戏

首先捋一下题意，题目是二人在都做出最优解得情况下，最后谁取得胜利
有几个关键点：

- 两个人都做出自认为的最优
- 两个人是没有区别的，智商一样，如果把他们谁放在先手，那么整个流程不会变，名字变了而已。

那么关键来了，对于从 i 到 j 的的子数组，进行选择的话，如果当前是A做出选择：
- 那么当前最优要么选择左边，要么选择右边
- 假设选择左边，那么剩下从 i + 1 到 j 的子数组，从B开始选。
**精髓来了**，B开始选，和A开始选是没有任何区别的，他们都会做出一样的决策。他们都是同样的人。也就是说当从 i + 1 到 j 的子数组 如果A先选，那么最终的结局绝对值之差和从B开始是一模一样的。

那么就得到了官方解得状态转移方程：
- 状态 dp[i][j] 定义：区间 piles[i..j] 内先手可以获得的相对分数；
- 状态转移方程：dp[i][j] = max(nums[i] - dp[i + 1, j] , nums[j] - dp[i, j - 1]) 。


```python3
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)
        dp = [[0] * length for _ in range(length)]
        for i, pile in enumerate(piles):
            dp[i][i] = pile
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][length - 1] > 0
```