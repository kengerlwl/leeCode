package 每日一题;

class Solution {
    public boolean validPartition(int[] nums) {
        int len = nums.length;
        if (len == 0 || len == 1) {
            if(len == 0) {
                return false;
            }
            return nums[0] == nums[1];
        }
        boolean[] dp = new boolean[len];
        dp[0] = false;

        if(nums[0] == nums[1]) {
            dp[1] = true;
        }else {
            dp[1] = false;
        }
        if(len ==2){
            return dp[1];
        }
        //长度为3的话
        
            if(nums[0] == nums[2] && nums[2] == nums[1]) {
                dp[2] = true;
            }else if((nums[2] - nums[1] == nums[1] - nums[0]) && nums[2] - nums[1] == 1) {
                dp[2] = true;
            }else{
                dp[2] = false;
            }
        

        for(int i =3; i < len; i++) {
            boolean flag2 = false;
            boolean flag3 = false;
            if(nums[i] == nums[i-1]) {
                flag2 = true;
            }
            if ((nums[i] - nums[i-1] == nums[i-1] - nums[i-2]) && (nums[i] - nums[i-1]) == 1) {
                flag3 = true;
            }
            if (nums[i] == nums[i-2] && nums[i] == nums[i-1]) {
                flag3 = true;
            }

            dp[i] = (dp[i-2] && flag2) || (dp[i-3] && flag3);
            
        }
        // 输出dp数组
        // for (int i = 0; i < len; i++) {
        //     System.out.println(dp[i]);
        // }
    return dp[len-1];

    }

}