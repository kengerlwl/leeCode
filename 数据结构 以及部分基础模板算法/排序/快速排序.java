// package 数据结构

// import java.lang.reflect.Array;
import java.util.Arrays;

class Solution {

    public static void quickSort(int[] nums, int start, int end) {
        if (end - start <= 1) {
            return;
        }
        int mid = partion(nums, start, end);
        quickSort(nums, start, mid - 1);
        quickSort(nums, mid + 1, end);
    }

    public static int partion(int[] nums, int start, int end) {
        if (end - start <= 1) {
            return start;
        }

        int left = start;
        int right = end;
        int midNum = nums[start];// 先把基准值拿出来

        // 先从右边找小于，再重左边找大于。
        while (left < right) {

            while (left < right && nums[right] >= midNum) {
                right--;
            }
            if (right - left == 0) {
                break;
            }
            nums[left] = nums[right];
            while (left < right && nums[left] <= midNum) {
                left++;
            }
            if (right - left == 0) {
                break;
            }
            nums[right] = left;
        }
        nums[left] = midNum;
        return left;

    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 4, 3, 2, 5, 6 };
        quickSort(nums, 0, nums.length - 1);
        System.out.println(Arrays.toString(nums));
    }

}
