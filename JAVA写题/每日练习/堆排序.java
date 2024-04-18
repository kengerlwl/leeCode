package 每日练习;

public class 堆排序 {

    public static int size;

    public static void heapSort(int[] nums) {
        for (int i = nums.length / 2; i >= 1; i--) {
            nodeDown(nums, i);
        }
    }

    public static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    // 假设是最小堆
    public static void nodeDown(int[] nums, int index) {
        int targetIndex = -1;
        int left = getLeft(index);
        int right = getRight(index);

        // 子节点更小的换上来。
        if (nums[left] < nums[index]) {
            targetIndex = left;
        }
        if (nums[right] < nums[index]) {
            targetIndex = right;
        }

        if (targetIndex == -1) {
            return;
        } else {
            swap(nums, targetIndex, index);
            nodeDown(nums, targetIndex);
        }

    }

    public static int getFather(int index) {
        return index / 2;
    }

    public static int getLeft(int index) {
        return index * 2;
    }

    public static int getRight(int index) {
        return index * 2 + 1;
    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 4, 3, 2, 5, 6 };
        System.out.println(nums);
        heapSort(nums);
        System.out.println(nums);
    }
}
