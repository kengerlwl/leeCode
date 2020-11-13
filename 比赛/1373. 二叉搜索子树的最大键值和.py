# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:

        @lru_cache(None)
        def dg(node):
            left = node.left
            right = node.right
            flag = True
            ans = node.val
            minV = node.val
            maxV = node.val
            if left:
                if left.val >= node.val:
                    flag = False
                    return flag, 0, 0, 0

                a, b, c, d = dg(left)

                if node.val <= d:
                    return False, 0, 0, 0

                minV = min(c, minV)
                maxV = max(d, maxV)
                flag = flag and a
                ans += b

            if right:
                if right.val <= node.val:
                    flag = False
                    return flag, 0, 0, 0
                a, b, c, d = dg(right)
                if node.val >= c:
                    return False, 0, 0, 0
                minV = min(c, minV)
                maxV = max(d, maxV)
                flag = flag and a
                ans += b

            return flag, ans, minV, maxV

        # print(dg(root))

        self.ans = 0
        queue = [root]
        flag = False
        while queue:
            newqueue = []
            for tmpNode in queue:

                f, v, c, d = dg(tmpNode)
                if f:
                    # print(v)
                    self.ans = max(self.ans, v)

                if tmpNode.left != None:
                    newqueue.append(tmpNode.left)
                if tmpNode.right != None:
                    newqueue.append(tmpNode.right)
            queue = newqueue
        return self.ans

        print(self.ans)