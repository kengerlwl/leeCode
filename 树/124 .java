class Solution {
    public int maxPathSum(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root.val;
        }
        else{
            int left = -9999999;
            if (root.left != null) {
                left = maxPathSum(root.left); // 左子树的最大路径和
            }
            int right = -9999999;
            if (root.right != null) {
                right = maxPathSum(root.right); // 右子树的最大路径和
            }
            
            int max = Math.max(left, right); 
            return Math.max( Math.max(maxToPath(root.left), 0) + Math.max(maxToPath(root.right), 0) + root.val, max);
        }
    }

    public int maxToPath(TreeNode root) {
        if (root == null) {
            return 0;
        }
        else{
            int left = maxToPath(root.left);
            int right = maxToPath(root.right);
            return Math.max(Math.max(left, right), 0) + root.val;
        }
    }
}