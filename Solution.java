import java.util.Scanner;

import 二维数组里面的二分.Solution;

public class Solution {

    public int target;

    public int[] searchRange(int[] nums, int target) {
        this.target = target;
        int left = binarySesarchLeft(nums, 0, nums.length);
        int right = binarySesarchRight(nums, 0, nums.length);

        return new int[] { left, right };
    }

    int binarySesarchLeft(int[] nums, int left, int right) {
        int mid = (left + right) / 2;
        if (left > right || left < 0 || right >= nums.length || nums.length == 0) {
            return -1;
        }
        if (nums[mid] == target) {
            if (mid > 0 && nums[mid] == nums[mid - 1]) {
                return binarySesarchLeft(nums, left, mid - 1);
            } else {
                return mid;
            }

        }
        if (nums[mid] > target) {
            return binarySesarchLeft(nums, left, mid - 1);
        } else {
            return binarySesarchLeft(nums, mid = 1, right);
        }
    }

    int binarySesarchRight(int[] nums, int left, int right) {
        int mid = (left + right) / 2;
        if (left > right || left < 0 || right >= nums.length || nums.length == 0) {
            return -1;
        }

        if (nums[mid] == target) {
            if (mid > 0 && nums[mid] == nums[mid + 1]) {
                return binarySesarchLeft(nums, mid + 1, right);
            } else {
                return mid;
            }

        }
        if (nums[mid] > target) {
            return binarySesarchLeft(nums, left, mid - 1);
        } else {
            return binarySesarchLeft(nums, mid = 1, right);
        }
    }

    // [5,7,7,8,8,10]
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Scanner sc = new Scanner(System.in);
        // System.out.println();
    }

}