// package 二维数组里面的二分;

// 通过结果进行二分。已知最大值和最小值，每次取mid。判断必mid小的数有多少个不难
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int left = matrix[0][0];
        int right = matrix[matrix.length - 1][matrix.length - 1];
        int mid = (left + right) / 2;
        int count;
        while (left < right) {
            mid = left + ((right - left) >> 1);
            count = countSmallerNum(matrix, mid, k);

            if (count < k) {
                left = mid + 1;
            } else if (count >= k) {
                right = mid;
            }

        }
        return left;
    }

    // 只能从左下角开始，因为右上角的数不一定比左下角的数大，而且小于mid的数有k个，不一定代表mid就是第k个数，这个是一个非递减，不等于递增。而且mid可能在矩阵中不存在
    public int countSmallerNum(int[][] matrix, int midValue, int k) {
        int count = 0;
        int n = matrix.length;
        int i = n - 1;
        int j = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] <= midValue) {
                count += i + 1;
                j++;
            } else {
                i--;
            }
        }
        return count;
    }

    // [[1,5,9],[10,11,13],[12,13,15]]
    public static void main(String[] args) {
        Solution s = new Solution();
        // [[1,5,9],[10,11,13],[12,13,15]]
        int[][] matrix = new int[][] { { 1, 5, 9 }, { 10, 11, 13 }, { 12, 13, 15 } };
        int k = 8;
        System.out.println(s.kthSmallest(matrix, k));
    }

}
//