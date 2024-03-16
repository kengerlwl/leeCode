import java.util.ArrayList;
import java.util.List;

class Solution {
    List<List<Integer>> ans;
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        ans = new ArrayList<>();

        back_tracking(candidates, target, new ArrayList<>(), 0, 0);
        return ans;
    }

    public void back_tracking(int[] nums, int target, List<Integer> lastList, int sum, int begin){
        if (sum == target) {
            List<Integer> temp = new ArrayList<>(lastList);
            ans.add(temp);
            return;
        }
        if(sum > target){
            return;
        }

        for(int i = begin; i < nums.length; i++){
            int tempSum = sum;
            int numOfi = (target - tempSum) / nums[i];
            for(int j = 1; j <= numOfi; j++){

                // add j 个 nums[i]
                for(int k = 0; k < j; k++){
                    lastList.add(nums[i]);
                    tempSum+=nums[i];
                }
                
                back_tracking(nums, target, lastList, tempSum, i+1);
                for(int k = 0; k < j; k++){
                    lastList.remove(lastList.size()-1);
                    tempSum-=nums[i];
                }
            }

        }
    }
}