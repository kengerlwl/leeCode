class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int ans =0;
        for(int i = 0; i < m ; i++){
            for(int j =0; j < n; j++){
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    ans++;
                    System.out.println("ans: " + ans);
                    System.out.println("i: " + i + " j: " + j);
                }
            }
        }

        return ans;
        
    }

    public void dfs(char[][] grid, int x, int y){
        int m = grid.length;
        int n = grid[0].length;

        
        if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == '1') {
            // if(grid[x][y] == '0'){
            //     return;
            // }
            System.out.println("x: " + x + " y: " + y);

            grid[x][y] = '0';
            dfs(grid, x, y-1);
            dfs(grid, x, y+1);
            dfs(grid, x+1, y);
            dfs(grid, x-1, y);
        }
        
    }

    // [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    public static void main(String[] args) {
        Solution s = new Solution();
        char[][] grid = new char[][]{
            {'1','1','1','1','0'},
            {'1','1','0','1','0'},
            {'1','1','0','0','0'},
            {'0','0','0','0','0'}
        };
        System.out.println(s.numIslands(grid));
    }

}