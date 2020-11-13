# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0

        @lru_cache(None)
        def dfs(node, pre):
            # print(count)

            # 上一个向左走
            if pre == 'left':
                nextNode = node.right
                if nextNode != None:
                    return 1 + dfs(nextNode, 'right')
                else:
                    return 1
            elif pre == 'right':
                nextNode = node.left
                if nextNode != None:
                    return 1 + dfs(nextNode, 'left')
                else:
                    return 1

        queue = [root]
        while queue:
            tmpNode = queue.pop()
            if tmpNode.left != None:
                queue.append(tmpNode.left)
            if tmpNode.right != None:
                queue.append(tmpNode.right)
            a = dfs(tmpNode, 'right')
            b = dfs(tmpNode, 'left')
            self.ans = max(self.ans,a,b)

        # dfs(root, 'right', 0)
        # # dfs(root, 'left', 0)
        # dfs(root.right, 'left', 0)
        print(self.ans-1)
        return self.ans -1