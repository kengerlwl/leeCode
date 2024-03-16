class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int[][] dp = new int[n + 1][n + 1]; // 前闭后开

        // 边界值是中间的线，找好边界和递归的方程很重要
        for (int j = 0; j < n; j++) {
            dp[j][j + 1] = 1;
        }
        int ans = 1;
        String ret = s.substring(0, 1);
        for (int j = 2; j <= n; j++) {
            for (int i = j - 2; i >= 0; i--) {
                if (j - i == 2) { // 长度为2；
                    if (s.charAt(i) == s.charAt(j - 1)) {
                        dp[i][j] = 2;
                    } else {
                        dp[i][j] = -1;
                    }
                }
                if (s.charAt(i) == s.charAt(j - 1) && dp[i + 1][j - 1] != -1) {
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    dp[i][j] = -1;
                }
                if (ans < dp[i][j]) {
                    ans = dp[i][j];
                    ret = s.substring(i, j);
                }

            }
        }

        return ret;

    }

    // "bb"
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.longestPalindrome("ac"));
    }
}