class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        boolean[] row = new boolean[m];
        boolean[] col = new boolean[n];
        // 遍历整个矩阵
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                // 如果当前位置是0
                if(matrix[i][j] == 0){
                    // 记录当前行和列需要置0
                    row[i] = true;
                    col[j] = true;
                }
            }
        }

        // 遍历整个矩阵
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                // 如果当前行或列需要置0
                if(row[i] || col[j]){
                    matrix[i][j] = 0;
                }
            }
        }
    }
}