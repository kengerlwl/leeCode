import java.util.LinkedList;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean isValidBST(TreeNode root) {
        // 判断左子树
        if (root.left != null) {
            if (root.left.val >= root.val) {
                return false;
            }
            else{
                if (!isValidBST(root.left)) {
                    return false;
                }
            }
        }

        // 判断右子树
        if (root.right != null) {
            if (root.right.val <= root.val) {
                return false;
            }
            else{
                if (!isValidBST(root.right)) {
                    return false;
                }
            }
        }

        return true;
    }


}