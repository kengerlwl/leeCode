package 数组;

class Solution {

    public int maxProfit(int[] prices) {
        int len = prices.length;
        if (len < 2) {
            return 0;
        }

        // 0：持有现金
        // 1：持有股票
        // 状态转移：0 → 1 → 0 → 1 → 0 → 1 → 0
        int[][] dp = new int[len][2]; 
        // dp[i][0]待办前i天，手上没有股票的最大利润
        // dp[i][1]待办前i天，手上持有股票的最大利润

        dp[0][0] = 0;
        dp[0][1] = -prices[0];

        for (int i = 1; i < len; i++) {
            // 这两行调换顺序也是可以的
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]); // 今天没有股票，要么是昨天就没有股票，要么是昨天有股票，今天卖了,如果今天卖了，那么就是昨天的持久股票的最大利润加上今天的股票价格
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }
        return dp[len - 1][0]; // 最后一定是手上没有股票的时候利润最大
    }
}
