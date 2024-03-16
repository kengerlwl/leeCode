class Solution {
    public void solve(char[][] board) {
        // 从边界开始搜索
        int m = board.length;
        int n = board[0].length;
        for(int i = 0; i < m; i++){
            dfs(board, i, 0);
            dfs(board, i, n-1);
        }
        for(int i = 0; i < n; i++){
            dfs(board, 0, i);
            dfs(board, m-1, i);
        }

        // 将所有的#变成O，所有的O变成X
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
                else if (board[i][j] == '#') {
                    board[i][j] = 'O';
                }
            }
        }
    }

    public void dfs(char[][] board, int x, int y){
        int m = board.length;
        int n = board[0].length;

        
        if (x >= 0 && x < m && y >= 0 && y < n && board[x][y] == 'O') {


            board[x][y] = '#';
            dfs(board, x, y-1);
            dfs(board, x, y+1);
            dfs(board, x+1, y);
            dfs(board, x-1, y);
        }
    }
}