import java.util.ArrayList;
import java.util.List;

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        List<TreeNode> pathP = new ArrayList<>();
        List<TreeNode> pathQ = new ArrayList<>();
        findPath(root, p, pathP);
        findPath(root, q, pathQ);
        
        int i = 0;
        while (i < pathP.size() && i < pathQ.size() && pathP.get(i) == pathQ.get(i)) {
            i++;
        }
        
        return pathP.get(i - 1);
    }
    

    // 这个算法思路还挺有用的，建议保留
    private boolean findPath(TreeNode root, TreeNode target, List<TreeNode> path) {
        if (root == null) return false;
        
        path.add(root);
        
        if (root == target) return true; // 前序遍历，通过删减list来实现保存指定路径
        
        if (findPath(root.left, target, path) || findPath(root.right, target, path)) {
            return true;
        }
        
        path.remove(path.size() - 1);
        return false;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}
