class Solution {
    public int sumNumbers(TreeNode root) {

    }

    public int dfs(TreeNode root, int preSum) {
        if (root == null) {
            return 0 + preSum;
        }
        else{
            int nowTotal = preSum * 10 + root.val;
            int ans = 0;
            if (root.left != null) {
                ans += dfs(root.left, nowTotal);
            }
            if (root.right != null) {
                ans += dfs(root.right, nowTotal);
            }
            if (root.left == null && root.right == null) {
                return nowTotal;
            }
            return ans;
        }
    }

}