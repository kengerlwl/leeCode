# 一次排除掉一半，但是不是进行分而治之

```
public int binarySearch(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2; // 避免left和right很大的时候溢出

        if (nums[mid] == target) {
            return mid; // 找到目标值，返回索引
        } else if (nums[mid] < target) {
            left = mid + 1; // 目标在右边
        } else {
            right = mid - 1; // 目标在左边
        }
    }

    return -1; // 目标值不存在
}

```


```
public int binarySearchRecursive(int[] nums, int target) {
    return binarySearch(nums, target, 0, nums.length - 1);
}

private int binarySearch(int[] nums, int target, int left, int right) {
    if (left > right) {
        return -1; // 目标值不存在
    }

    int mid = left + (right - left) / 2;

    if (nums[mid] == target) {
        return mid; // 找到目标值，返回索引
    } else if (nums[mid] < target) {
        return binarySearch(nums, target, mid + 1, right); // 目标在右边
    } else {
        return binarySearch(nums, target, left, mid - 1); // 目标在左边
    }
}

```





# 二分查找，上下界查找
例如左查找，
如果有目标值，返回目标值最左边的下标（因为可能有多个）。
如果没有目标值，那么返回刚好比目标值大的那个值的下标，（相当于插入点）


```
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

    public static void main(String[] args) {
        int[] arr = { 0, 2, 2, 2, 3, 4, 5 };
        int target = 6;

        int leftBound = findLeftBound(arr, target);
        int rightBound = findRightBound(arr, target);

        System.out.println("Left Bound Index: " + leftBound);
        System.out.println("Right Bound Index: " + rightBound);
    }
}

```


调用库现成。

```
import java.util.Arrays;

public class BinarySearchExample {
    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 10, 40};
        int key = 10;

        int result = Arrays.binarySearch(arr, key); //如果Arrays.binarySearch()方法未找到目标元素，它将返回一个负数值。具体来说，如果目标元素不在数组中，则返回的负数值为 -(insertion point) - 1。插入点是指在数组中应该插入目标元素的索引位置，以保持数组的排序顺序。

        if (result >= 0) {
            System.out.println("Element found at index " + result);
        } else {
            int insertionPoint = -(result + 1);
            if (insertionPoint < arr.length && arr[insertionPoint] == key) {
                System.out.println("Element found at index " + insertionPoint);
            } else {
                System.out.println("Element not found in the array");
                System.out.println("Insertion point is at index " + insertionPoint);
                if (insertionPoint < arr.length) {
                    System.out.println("Next greater element is at index " + insertionPoint + ", value: " + arr[insertionPoint]);
                }
            }
        }
    }
}

```