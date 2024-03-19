import java.util.Scanner;
import java.util.Arrays;

class CustomBinarySearch {
    public static int findLeftBound(int[] arr, int target) {
        int low = 0;
        int high = arr.length;

        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }

    public static int findRightBound(int[] arr, int target) {
        int low = 0;
        int high = arr.length;

        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target) {
                low = mid;
            }
            if (arr[mid] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }

        return low;
    }
}

// 注意类名必须为 Main, 不要有任何 package xxx 信息
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = in.nextInt();
        }
        int k = in.nextInt();
        for (int i = 0; i < k; i++) {
            int left = in.nextInt();
            int right = in.nextInt();
            int target = in.nextInt();
            int l1 = CustomBinarySearch.findLeftBound(nums, target);
            int r1 = CustomBinarySearch.findRightBound(nums, target);
            // 没有target, 或者不在区间
            if (nums[l1] != target || l1 > right || r1 < left) {
                System.out.println(0);
                continue;
            }

            // 完全是子区间
            if (l1 >= left && r1 <= right) {
                System.out.println(r1 - l1 + 1);
                continue;
            } else { // 有交接
                if (l1 > left) {
                    System.out.println(right - l1 + 1);
                } else {
                    System.out.println(r1 - left + 1);
                }
            }

            // 半个

        }
    }
}