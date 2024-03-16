package 数组;

class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int now = 0;
        int[] dp = new int[n];
        dp[0] = nums[0];
        if(n == 1){
            return true;
        }
        if(dp[0] == 0){
            return false;
        }
        
        for (int i = 1; i < n; i++) {
            
            dp[i] = Math.max(dp[i - 1] - 1, nums[i]);
            if (dp[i] == 0 && i != n - 1) {
                return false;
            }
        }

        if (dp[n - 1] >= 0) {
            return true;
        } else {
            return false;
            
        }
        
        
    }
}