package 每日一题;

class Solution {
    public int minIncrements(int n, int[] cost) {
        

        // 精髓，巧妙的将要到最后一层每个节点的值都增加到最大值，（通过给该层的父节点增加下一层的最大数值）转化为了到倒数第二层的每个节点的值都增加到最大值
        
        int ans  =0 ;
        for(int i = n/2; i >= 1; i--){
            int left = i*2;
            int right = i*2+1;
            // 如果左右子节点的路径和大于父节点的路径和，那么需要增加父节点的值
            ans += Math.abs(cost[left-1] - cost[right-1]);
            cost[i-1] += Math.max(cost[left-1], cost[right-1]);
        }
        return ans; 

    }

//     n =
// 7
// cost =
// [1,5,2,2,3,3,1]
    public static void main(String[] args) {
        Solution s = new Solution();
        int n = 7;
        int[] cost = {1,5,2,2,3,3,1};
        System.out.println(s.minIncrements(n, cost));
    }

}