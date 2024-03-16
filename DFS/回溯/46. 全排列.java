package DFS.回溯;
import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<List<Integer>> ans;
    public List<Boolean> vis;
    public int orgin_k ;
    public List<List<Integer>> permute(int[] nums) {
        List<Integer> temp = new ArrayList<Integer>(nums.length);
        for(int i =0; i < nums.length; i++){
            temp.set(i, nums[i]);
        }
        back_tracking(temp, nums.length, new ArrayList<>());
        return ans;
        
    }
    // 剩下k个数字组合， 由于要的是不带顺序的组合数，那么相当于要对原有答案去重。
    public void back_tracking(List<Integer> nums, int k, List<Integer> lastNums){
        if (k == 0) {
            ans.add(new ArrayList<>(lastNums));
        }else{
            for(int i =0; i < nums.size(); i++){

               
                List<Integer> temp = new ArrayList<>(nums);
                temp.remove(i);
                lastNums.add(nums.get(i));
                back_tracking(temp, k-1, lastNums);
                lastNums.remove(lastNums.size()-1); // 回溯
                // if (k == ) {
                    
                // }
             
            }
            
        }

    }
}