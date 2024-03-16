class Solution {
    public int findMin(int[] nums) {
        return binarySesarch(nums, 0, nums.length - 1);
    }

    public int binarySesarch(int[] nums, int left, int rihgt) {
        int mid = (left + rihgt) / 2;
        if (left > rihgt) {
            return -1;
        }

        // left is order
        if (nums[mid] > nums[left]) {
            return Math.min(nums[left], binarySesarch(nums, mid + 1, rihgt));
        } else {
            return Math.min(nums[mid], binarySesarch(nums, left, mid - 1));
        }
    }
}