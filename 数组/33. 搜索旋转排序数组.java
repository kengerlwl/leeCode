package 数组;


// 实现了时间复杂度为O(logn)的算法，关键就是利用二分查找。
// 左右必有一边是绝对有序的。那么可以根据有序一边的极值来判断target在不在这一边，如果在，就继续在这一边找，如果不在，就在另一边找。
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        return find(nums, target, left, right);

    }

    public int find(int[] nums, int target, int left, int right) {
        // 找不到
        if (left > right) {
            return -1;
        }
        int mid = (left + right) / 2;
        if (nums[mid] == target) {
            return mid;
        }
        // 如果左边有序
        if (nums[left] <= nums[mid]) {
            // 在范围内
            if (target >= nums[left] && target <= nums[mid]) {
                return find(nums, target, left, mid);
            } else {
                return find(nums, target, mid + 1, right);
                
            }
        }
        else { // 左边无序，右边有序
            if (target >= nums[mid] && target <= nums[right]) { // 看要不要找右边
                return find(nums, target, mid+1, right);
            } else {
                return find(nums, target, left, mid);
            }
        }
        
            
        

    }
}