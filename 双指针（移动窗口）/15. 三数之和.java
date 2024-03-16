import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        for(int i = 0; i < n; i++){
            int left = i + 1;
            int right = n - 1;
                            while(i < n-1 && nums[i] == nums[i+1]){
                    i++;

                }
            while (left < right) {
                
                if (nums[i] + nums[left] + nums[right] == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    // 要跳过重复的元素
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                        // i = left;
                    }
                }
                else if (nums[i] + nums[left] + nums[right] < 0) {
                    left++;
                }
                else if (nums[i] + nums[left] + nums[right] > 0) {
                    right--;
                }

            }
        }
        return res;
    }
}