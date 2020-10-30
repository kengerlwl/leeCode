# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 还是和之前一样，做抢和不抢的选择。
class Solution:
    def rob(self, root: TreeNode) -> int:
        # dp解法，建立两个表（哈希表映射）
        # 函数f(node)为打劫当前节点node时的最大收益
        # 函数g(node)为不打劫当前节点node时的最大收益
        # 两种情况：
        # 1 当前节点被打劫，则其左子节点和右子节点没有被打劫:
        #   f(node)=g(node.left)+g(node.right)+node.val
        # 2 当前节点没有被打劫，则其左子节点和右子节点可以被打劫或不打劫:
        #   g(node)=max(f(node.left),g(node.left))+max(f(node.right),g(node.right))
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            f[root] = g[root.left] + g[root.right] + root.val
            g[root] = max(f[root.left], g[root.left]) + max(f[root.right], g[root.right])

        f = {None: 0}
        g = {None: 0}
        dfs(root)
        return max(f[root], g[root])

