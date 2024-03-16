package 数组;

import java.lang.reflect.Array;

// 上升就按照+1来，下降就直接下降到1，然后再从1开始上升。

// 分为左右两个递增的规则，注意，必须是递增才方便后面取最大值的逻辑
class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] left = new int[ratings.length];
        int[] right = new int[ratings.length];

        // 对left计算满足左规则的值
        left[0] = 1;
        for(int i = 0; i < n-1; i++){
            if(ratings[i+1] > ratings[i]){
                left[i+1] = left[i] + 1;
            }else{
                left[i+1] = 1;
            }
        }


        // 对right计算满足右规则的值，前提是不破坏左规则
        right[n-1] = left[n-1];

        for(int j = n-2; j >= 0; j--){
            if(ratings[j] > ratings[j+1]){ // 如果需要向左递增，那么要比右边的值大，且不能破坏左规则（多增加几个数不会破坏左规则。）那么在满足右规则的情况下，取两个的最大值
                right[j] = Math.max(left[j], right[j+1]+1);
            }else{
                right[j] = left[j];
            }
        }
        int ans =0;
        // 对right求和
        for(int i = 0; i < n; i++){
            ans += right[i];
        }
        return ans;

    }
}