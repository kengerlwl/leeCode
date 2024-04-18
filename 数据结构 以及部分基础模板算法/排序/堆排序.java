public class Solution {

    public static int size;

    public static void heapSort(int[] nums) {
        size = nums.length;

        // 构建最小堆
        for (int i = nums.length / 2 - 1; i >= 0; i--) {
            nodeDown(nums, i);
        }

        // 依次将堆顶元素（最小值）与最后一个元素交换，并调整堆
        for (int i = nums.length - 1; i >= 0; i--) {
            swap(nums, 0, i);
            size--; // 堆大小减1，忽略已排序的元素
            nodeDown(nums, 0);
        }
    }

    public static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    // 假设是最小堆
    public static void nodeDown(int[] nums, int index) {
        int targetIndex = index;
        int left = getLeft(index);
        int right = getRight(index);

        if (left < size && nums[left] < nums[targetIndex]) {
            targetIndex = left;
        }
        if (right < size && nums[right] < nums[targetIndex]) {
            targetIndex = right;
        }

        if (targetIndex != index) {
            swap(nums, targetIndex, index);
            nodeDown(nums, targetIndex);
        }
    }

    public static int getFather(int index) {
        return (index - 1) / 2;
    }

    public static int getLeft(int index) {
        return index * 2 + 1;
    }

    public static int getRight(int index) {
        return index * 2 + 2;
    }

    public static void printHeap(int[] nums) {
        for (int num : nums) {
            System.out.print(num + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] nums = new int[] { 1, 4, 3, 2, 5, 6 };
        printHeap(nums);
        heapSort(nums);
        printHeap(nums);
    }
}

// 对于下标从0开始的映射关系
// left: 2*i +1
// right: 2*i +2
// father: (i-1) /2