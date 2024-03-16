class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n = s1.length();
        int m = s2.length();
        boolean[][] dp = new boolean[n + 1][m + 1]; // 对于这种需要左上角所有的值的，都是从0开始的。就一行一行，从左到右构建转移顺序
        dp[0][0] = true;
        if (n + m != s3.length()) {
            return false;
        }
        if (n == 0) {
            return s2.equals(s3);
        }
        if (m == 0) {
            return s1.equals(s3);
        }

        for (int i = 1; i <= n; i++) {
            if (s3.charAt(i - 1) == s1.charAt(i - 1)) {
                dp[i][0] = dp[i - 1][0];
            }
        }

        for (int j = 1; j <= m; j++) {
            if (s3.charAt(j - 1) == s2.charAt(j - 1)) {
                dp[0][j] = dp[0][j - 1];
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                int k = i + j - 1;
                if (s3.charAt(k) == s1.charAt(i - 1)) {
                    dp[i][j] = dp[i - 1][j];
                }
                if (s3.charAt(k) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i][j] || dp[i][j - 1];
                }
            }
        }

        return dp[n][m];
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"));
    }
}
