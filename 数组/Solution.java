public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        int[] preDot = new int[n];
        int[] postDot = new int[n]; // 后缀乘积
        preDot[0] = nums[0];
        postDot[n-1] = nums[n-1];
        for(int i = 1; i < n; i++) {
            preDot[i] = preDot[i-1] * nums[i];
        }
        for(int i = n-2; i >= 0; i--) {
            postDot[i] = postDot[i+1] * nums[i];
        }
        for(int i = 0; i < n; i++) {
            if(i == 0){
                answer[i] = postDot[i];
                continue;
            }
            if(i == n-1) {
                answer[i] = preDot[i];
                continue;
            }
            answer[i] = preDot[i] * postDot[i];
        }
        return answer;

    }

    //[1,2,3,4]

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {1,2,3,4};
        int[] res = s.productExceptSelf(nums);
        for(int i = 0; i < res.length; i++) {
            System.out.println(res[i]);
        }
    }
}