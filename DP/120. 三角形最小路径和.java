import java.util.ArrayList;
import java.util.List;

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[][] dp = new int[n + 1][n + 1];
        dp[0][0] = triangle.get(0).get(0);
        int ans = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                dp[i][j] = Integer.MAX_VALUE;
                if (j < triangle.get(i - 1).size()) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][j] + triangle.get(i).get(j));
                }
                if (j > 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[i - 1][j - 1] + triangle.get(i).get(j));
                }

                if (i == n - 1) {
                    ans = Math.min(ans, dp[i][j]);
                }
            }
        }
        if (n == 1) {
            return dp[0][0];

        }
        return ans;

    }

    // [[2],[3,4],[6,5,7],[4,1,8,3]]
    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<Integer>> triangle = new ArrayList<>();
        List<Integer> l1 = new ArrayList<>();
        l1.add(2);
        List<Integer> l2 = new ArrayList<>();
        l2.add(3);
        l2.add(4);
        List<Integer> l3 = new ArrayList<>();
        l3.add(6);
        l3.add(5);
        l3.add(7);
        List<Integer> l4 = new ArrayList<>();
        l4.add(4);
        l4.add(1);
        l4.add(8);
        l4.add(3);
        triangle.add(l1);
        triangle.add(l2);
        triangle.add(l3);
        triangle.add(l4);
        System.out.println(s.minimumTotal(triangle));
    }
}