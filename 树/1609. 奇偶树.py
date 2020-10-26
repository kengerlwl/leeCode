# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import queue
        q = queue.Queue
        q.put(root)
        deep =0  # 深度
        while q.empty():
            tmpq = queue.Queue

            for i in range(q.qsize()-1):
                qt =q.queue
                if deep % 2 != 0:
                    if qt[i].val <= qt[i + 1].val:
                        flag = False
                else:
                    if qt[i].val >= qt[i + 1].val:
                        flag = False

            while q.empty():
                node = q.get()
                if node.val % 2 == deep % 2:  # 遍历所有节点判断node的值和深度奇偶性是否不同
                    flag = False
                if node.left:
                    tmpq.append(node.left)  # 把下一层左子节点加加入到队列中
                if node.right:
                    tmpq.append(node.right)  # 把下一层右子节点加加入到队列中
            deep += 1
            queue = tmpq






# Solution.isEvenOddTree(None, )