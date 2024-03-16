import java.sql.Array;
import java.util.Arrays;

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
    public TreeNode buildTree(int[] preorder, int[] inorder) {

        if (preorder.length == 0) {
            return null;
        }
        if (preorder.length == 1) {
            return new TreeNode(preorder[0]);
        }

        int rootVal = preorder[0];
        TreeNode root = new TreeNode(rootVal);
        int rootIndex = 0;
        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == rootVal) {
                rootIndex = i;
                break;
            }
        }

        int [] leftInorder = Arrays.copyOfRange(inorder, 0, rootIndex);
        int [] rightInorder = Arrays.copyOfRange(inorder, rootIndex + 1, inorder.length);
        int [] leftPreorder = Arrays.copyOfRange(preorder, 1, rootIndex + 1);
        int [] rightPreorder = Arrays.copyOfRange(preorder, rootIndex + 1, preorder.length);
        TreeNode left = buildTree(leftPreorder, leftInorder);
        TreeNode right = buildTree(rightPreorder, rightInorder);
        root.left = left;
        root.right = right;
        return root;

    }
}