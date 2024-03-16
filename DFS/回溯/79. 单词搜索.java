class Solution {
    public boolean ans = false;
    public boolean[][] vis;
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        vis = new boolean[m][n];
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(board[i][j] == word.charAt(0)){
                    dfs(board, word, i, j, 0);
                    if(ans){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public void dfs(char[][] board, String word, int x, int y, int index){
        if(ans){
            return;
        }
        if(index == word.length()){
            ans = true;
            return;
        }
        int m = board.length;
        int n = board[0].length;
        if(x >= 0 && x < m && y >= 0 && y < n && !vis[x][y] && board[x][y] == word.charAt(index)){
            vis[x][y] = true;
            dfs(board, word, x, y-1, index+1);
            dfs(board, word, x, y+1, index+1);
            dfs(board, word, x-1, y, index+1);
            dfs(board, word, x+1, y, index+1);
            vis[x][y] = false;
        }
    }
}