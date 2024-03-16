class Solution {
    public boolean isValidSudoku(char[][] board) {
        // 用三个数组分别记录每一行、每一列、每一个九宫格中的数字出现的次数
        int[][] row = new int[9][9];
        int[][] col = new int[9][9];
        int[][] box = new int[9][9];
        // 遍历整个数独
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                // 如果当前位置是数字
                if(board[i][j] != '.'){
                    int num = board[i][j] - '0' - 1;
                    int boxIndex = (i / 3) * 3 + j / 3;
                    // 如果当前数字在行、列、九宫格中出现过，返回false
                    if(row[i][num] == 1 || col[j][num] == 1 || box[boxIndex][num] == 1){
                        return false;
                    }
                    // 记录当前数字出现过
                    row[i][num] = 1;
                    col[j][num] = 1;
                    box[boxIndex][num] = 1;
                }
            }
        }
        return true;
    }
}