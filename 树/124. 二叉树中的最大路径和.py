# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 1

        def treeBL(node):

            if node == None:
                return 0
            left = max(0, treeBL(node.left))
            right = max(0, treeBL(node.right))
            nonlocal ans
            ans = max(ans, (left+ right+node.val))
            return max(left, right)+node.val


        treeBL(root)
        print(ans)
        return ans
Solution.maxPathSum(None,None)