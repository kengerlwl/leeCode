# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        # 计算next数组， next[i]代表前i个字符串的最长子串
        def getnext(s):
            n = len(s)
            next = [0, 0]  # 第一个0代表空字符串
            for i in range(2, n + 1):
                # print(next, s, i-1)
                if s[next[i - 1]] == s[i - 1]:
                    next.append(next[i - 1] + 1)
                else:
                    j = next[next[i - 1]]
                    while j > 0:
                        if s[j] == s[i - 1]:
                            next.append(j + 1)
                            break
                        j = next[j]
                    if j == 0:
                        if s[i - 1] == s[0]:
                            next.append(1)
                        else:
                            next.append(0)

            return next

        needle = []
        while head:
            needle.append(head.val)
            head = head.next

        next = getnext(needle)
        print(next)

        # 构造有限状态机
        def kmp(s, next):  # 一个状态机
            n = len(s)
            state = {'other': True}
            for i in s:
                state[i] = True

            matrix = [{} for i in range(n + 1)]

            # 初始化
            for i in state:
                matrix[0][i] = 0
            matrix[0][s[0]] = 1

            # 归纳法进行递推
            for i in range(1, n + 1):

                j = i
                while j > 0:
                    if j >= n:
                        j = next[j]
                        continue
                    char = s[j]
                    if char not in matrix[i]:
                        matrix[i][char] = j + 1
                    j = next[j]
                if j == 0:
                    if s[0] not in matrix[i]:
                        matrix[i][s[0]] = 1
                for k in state:
                    if k not in matrix[i]:
                        matrix[i][k] = 0
            return matrix, state

        matrix, state = kmp(needle, next)
        print(matrix)
        self.flag = False



        # kmp

        def dfs(stateNow, node):
            # print(node.val,stateNow,len(needle))
            val = node.val
            statetmp = None
            if stateNow == len(needle):
                self.flag = True

            if val in matrix[stateNow]:
                statetmp = matrix[stateNow][val]
            else:
                statetmp = matrix[stateNow]['other']
            if statetmp == len(needle):
                self.flag = True
            if node.left:
                dfs(statetmp, node.left)
            if node.right:
                dfs(statetmp, node.right)

        dfs(0, root)
        print(self.flag)
        if self.flag:
            return self.flag
        else:
            return False
        # return False


