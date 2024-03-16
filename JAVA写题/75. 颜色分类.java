import java.util.Arrays;
class Solution {
    public void sortColors(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int index = 0;
        while (index<=right) {
            if (nums[index] == 0) {
                swap(nums, index, left);
                left++;
                index++;
            } else if (nums[index] == 2) {
                swap(nums, index, right);
                right--;
            } else {
                index++; // 不用管1怎么移动，因为0和2在移动的时候，1会自动移动到中间
                
            }
        }
}
    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

}
