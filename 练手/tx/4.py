# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        flag = True

        if p == q == None:
            return True
        elif q == None or p == None:
            return False


        if p.val != q.val:
            flag = False

        f = self.isSameTree(p.left, q.left)
        
        f2 = self.isSameTree(p.right, q.right)

        flag = flag and  f and f2

        return flag