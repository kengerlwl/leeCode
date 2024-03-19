class maxHeap {

    // 数组
    public int[] nums;
    public int size;

    maxHeap(int[] nums, int size) {
        this.nums = nums;
        this.size = size;
    }

    public void printHeap() {

        // 打印
        int level = 1;
        int index = 1;
        while (index <= size) {
            for (int i = 0; i < level; i++) {
                if (index <= size) {
                    System.out.print(nums[index] + " ");
                    index++;
                }
            }
            System.out.println();
            level *= 2;
        }
    }

    // 构建堆
    public void buildHeap() {
        for (int i = size / 2; i >= 1; i--) {
            // nodeUp(i); // 构建堆上浮会构建失败
            nodeDown(i); // 下沉构建
        }
    }

    public int popMax() {

        if (size <= 0) {
            return -1;// pop出最大值
        }
        int ans = nums[1];
        swap(1, size);
        size--;
        nodeDown(1);

        return ans;
    }

    // 上浮
    public void nodeUp(int index) {
        int father = getFather(index);

        while (father > 0 && nums[index] > nums[father]) {
            swap(index, father);
            index = father;
            father = getFather(index);
        }
    }

    public void nodeDown(int index) {
        int left = getLeft(index);
        int right = getRight(index);
        int maxIndex = index;
        if (left <= size && nums[left] > nums[maxIndex]) {
            maxIndex = left;
        }
        if (right <= size && nums[right] > nums[maxIndex]) {
            maxIndex = right;
        }
        if (maxIndex != index) {
            swap(index, maxIndex);
            nodeDown(maxIndex);
        }
    }

    public int getFather(int index) {
        return (int) (index / 2);
    }

    public int getLeft(int index) {
        return index * 2;
    }

    public int getRight(int index) {
        return index * 2 + 1;
    }

    public void swap(int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

}

class Solution {

    public int findKthLargest(int[] nums, int k) {
        // 构建堆
        int[] temp = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            temp[i + 1] = nums[i];
        }
        maxHeap m = new maxHeap(temp, nums.length);
        m.buildHeap();
        // m.printHeap();
        int ans = 0;
        for (int i = 0; i < k; i++) {
            ans = m.popMax();
            System.out.println("ans: " + ans);
            // m.printHeap();
        }
        return ans;
    }

    // [3,2,1,5,6,4], k = 2
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = new int[] { 3, 2, 1, 5, 6, 4 };
        System.out.println(s.findKthLargest(nums, 2));
    }
}