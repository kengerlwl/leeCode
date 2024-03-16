package 数组;

class Solution {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        int[][] dp = new int[len][len]; // 实际上只需要一维数组既可以
        int [] minPre = new int[len];
        int nowMin = 9999999;
        // 找出前n个最小值
        for(int i=0; i< len; i++){
            if(prices[i] < nowMin){
                nowMin = prices[i];
                minPre[i] = nowMin;
            }
        }
        // 初始化边界条件
        for(int i=0; i<len; i++){
            dp[i][0] = 0;
        }
        int ans = 0;
        for(int i=1; i<len; i++){
            for(int j =1; j<len; j++){
                dp[i][j] = Math.max(dp[i][j-1], prices[j] - minPre[j-1]);
                if (dp[i][j] > ans){
                    ans = dp[i][j];
                }
            }
        }
        return ans;
    }


    
    // [7,1,5,3,6,4]

// public static void main(String[] args) {
//     // 这里是程序的入口点
//     Solution s = new Solution();
//     int[] prices = {7,1,5,3,6,4};
//     System.out.println(s.maxProfit(prices));
// }

}


