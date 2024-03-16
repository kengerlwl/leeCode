import java.util.ArrayList;
import java.util.List;


// 这道题目是一个典型的广度优先搜索的题目，通过广度优先搜索，我们可以找到最短路径
class Solution {
    public int snakesAndLadders(int[][] board) {
        List<Integer> q = new ArrayList<>();
        q.add(1);
        int n = board.length;
        
        boolean[] visited = new boolean[n * n + 1];
        int step = 0;
        // 使用广度优先搜索
        while (q.size() !=0) {

            int size = q.size();
            for(int i = 0; i < size; i++) {
                int cur = q.remove(0);
                if (visited[cur]) {
                    continue;
                }
                visited[cur] = true;
                if (cur == n * n) {
                    return step;
                }
                for(int j = 1; j <= 6 && cur + j <= n * n; j++) {
                    int next = cur + j;
                    int[] pos = getPosition(next, n);
                    if (board[pos[0]][pos[1]] != -1) {
                        next = board[pos[0]][pos[1]];
                    }
                    q.add(next);
                }
            }
            step++;
        }
        return -1;

    }

    // 这个函数是用来计算当前数字在棋盘上的位置
    public int[] getPosition(int num, int n) {
        int r = (num - 1) / n;
        int x = n - 1 - r;
        int y = (r % 2 == 0) ? (num - 1) % n : n - 1 - (num - 1) % n;
        return new int[]{x, y};
    }
}