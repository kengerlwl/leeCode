// 这个题目也可以用二分法
// 但是我选择前缀和的方法

class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] matrixPresum = new int[m + 1][n + 1];
        matrixPresum[0][0] = matrix[0][0] - '0';
        int ans = 0;
        for (int j = 1; j < n; j++) {
            matrixPresum[0][j] = matrixPresum[0][j - 1] + matrix[0][j] - '0';
            if (matrix[0][j] == '1') {
                ans = 1;
            }

        }
        for (int i = 1; i < m; i++) {
            matrixPresum[i][0] = matrixPresum[i - 1][0] + matrix[i][0] - '0';
            if (matrix[i][0] == '1') {
                ans = 1;
            }
        }

        // 前缀和计算完毕
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                matrixPresum[i][j] = matrixPresum[i - 1][j] + matrixPresum[i][j - 1] - matrixPresum[i - 1][j - 1]
                        + matrix[i][j] - '0';
            }
        }

        int size = Math.min(m, n);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 1; k <= size; k++) {
                    int newI = i + k - 1;
                    int newJ = j + k - 1;
                    if (newI >= m || newJ >= n) {
                        break;
                    }
                    int sum = matrixPresum[newI][newJ];
                    if (i > 0) {
                        sum -= matrixPresum[i - 1][newJ];
                    }
                    if (j > 0) {
                        sum -= matrixPresum[newI][j - 1];
                    }
                    if (i > 0 && j > 0) {
                        sum += matrixPresum[i - 1][j - 1];
                    }
                    if (sum == k * k) {
                        ans = Math.max(ans, sum);
                    }

                }
            }
        }

        return ans;
    }

    // matrix =
    // [["0","1","1","0"],["0","0","0","0"],["0","0","1","0"],["0","1","0","1"],["0","0","0","1"],["0","0","1","0"]]
    public static void main(String[] args) {
        Solution s = new Solution();
        char[][] matrix = new char[][] { { '0', '1', '1', '0' }, { '0', '0', '0', '0' }, { '0', '0', '1', '0' },
                { '0', '1', '0', '1' }, { '0', '0', '0', '1' }, { '0', '0', '1', '0' } };
        System.out.println(s.maximalSquare(matrix));
    }

}