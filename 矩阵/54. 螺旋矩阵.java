import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        int x = 0 ,y = 0;
        List<List<Integer>> toward = new ArrayList<>(); 
        // toward.addAll(new int[]{0, 1}); // 向右
        // toward.addAll(new int[]{1, 0}); // 向下
        // toward.addAll(new int[]{0, -1}); // 向左
        // toward.addAll(new int[]{-1, 0}); // 向上
        toward.add(new ArrayList<Integer>(){{add(0); add(1);}});
        toward.add(new ArrayList<Integer>(){{add(1); add(0);}});
        toward.add(new ArrayList<Integer>(){{add(0); add(-1);}});
        toward.add(new ArrayList<Integer>(){{add(-1); add(0);}});
        int[][] visited = new int[m][n];
        int i = 0;  // 代表是第几次转向
        while(i < m * n){
            res.add(matrix[x][y]);
            visited[x][y] = 1;
            int nextX = x + toward.get(i % 4).get(0);
            int nextY = y + toward.get(i % 4).get(1);
            if(nextX < 0 || nextX >= m || nextY < 0 || nextY >= n || visited[nextX][nextY] == 1){ //如果下一个位置越界或者已经访问过
                i++;
                if (res.size() >0 && res.size() != m * n) {
                    res.remove(-1);
                }
            }else{
                x = nextX;
                y = nextY;
                
                
            }
        }
        return res;
        

        

    }
}