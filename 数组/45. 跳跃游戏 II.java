package 数组;


class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = 0;
        int j = 0; // 用于记录上一个可以到达当前位置的位置，由于每次到达的位置都是最远的位置，所以不需要担心j的值会变小，减少内循环的遍历次数。我这个优化很成功，时间复杂度从O(n^2)降到了O(n)
        for(int i = 1; i < n; i++){
            while (j < i){
                if(j + nums[j] >= i){
                    dp[i] = dp[j] + 1;
                    break;
                }
                j++;
            }
        }

        return dp[n - 1];

    }
}