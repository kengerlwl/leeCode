
//你必须实现时间复杂度为 O(log n) 的算法来解决此问题。


class Solution {
    public int length;
    public int findPeakElement(int[] nums) {
        length = nums.length;
        return binarySesarch(nums, 0, length-1);
    }

    public int binarySesarch(int[] nums, int left, int right){
        int mid = (left + right)/2;

        if (left == right) { 
            return left;
        }

        if (left == 0 && right == 1) {
            if (nums[mid] > nums[right]) {
                return 0;
            }
        }

        if (right == nums.length-1 && left == right-1) {
            if (nums[right] > nums[left]) {
                return nums.length-1;
            }
        }


        if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1]) {
            return mid;
        }

        // left lager, turn left
        if (nums[mid-1] > nums[mid]) {
            return binarySesarch(nums, left, mid);
        }else{
            return binarySesarch(nums, mid+1, right);
        }
    }
}