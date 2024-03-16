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