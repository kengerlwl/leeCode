class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left_node = None
        self.right_node = None


# 给定二叉树的前序遍历和中序遍历，获得该二叉树
def getBSTwithPreTin(pre, tin):
    if len(pre) == 0 | len(tin) == 0:
        return None
    root = TreeNode(pre[0])
    for order, item in enumerate(tin):
        if root.val == item:
            root.left_node = getBSTwithPreTin(pre[1:order + 1], tin[:order])
            root.right_node = getBSTwithPreTin(
                pre[order + 1:], tin[order + 1:])
            return root


def listcreattree(root, llist, i):  # 用列表递归创建二叉树，
    # 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
    # 再接着创建b的右子树，
    if i < len(llist):
        if llist[i] == '#':
            return None  # 这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left_node = listcreattree(
                root.left_node, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right_node = listcreattree(
                root.right_node, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  # 这里的return很重要
    return root


# 二叉树按层序转换为列表
def treeArray(pRoot):
    if not pRoot:
        return []
    resultList = []
    curLayer = [pRoot]
    while curLayer:
        curList = []
        nextLayer = []
        for node in curLayer:
            if node == '.':
                curList.append('.')
            else:
                curList.append(node.val)
                if node.left_node:
                    nextLayer.append(node.left_node)
                else:
                    nextLayer.append('.')
                if node.right_node:
                    nextLayer.append(node.right_node)
                else:
                    nextLayer.append('.')
        resultList.append(curList)
        curLayer = nextLayer
    return resultList


# 打印为树状图
def toTree4(t):
    n = len(t) - 1
    for i in range(1, n - 1):
        for j in range(2 * i):
            if t[i][j] == '.':
                t[i + 1].insert(j + 1, '.')
                t[i + 1].insert(j + 1, '.')
    result = []
    result.append('       {}       '.format(t[0][0]))
    result.append('    /     \\    ')
    result.append('   {}       {}   '.format(t[1][0], t[1][1]))
    result.append('  / \\     / \\  ')
    result.append(' {}   {}   {}   {} '.format(*t[2]))
    result.append('/ \\ / \\ / \\ / \\')
    result.append(' '.join([str(i) for i in t[3]]))
    for i in result[:2 * n - 1]:
        print(i)


# 深度小于等于3
def toTree3(t):
    n = len(t) - 1
    for i in range(1, n - 1):
        for j in range(2 * i):
            if t[i][j] == '.':
                t[i + 1].insert(j + 1, '.')
                t[i + 1].insert(j + 1, '.')
    result = []
    result.append('   {}   '.format(t[0][0]))
    result.append('  / \\  ')
    result.append(' {}   {} '.format(t[1][0], t[1][1]))
    result.append('/ \\ / \\')
    result.append('{} {} {} {}'.format(*t[2]))
    for i in result[:2 * n - 1]:
        print(i)


# 将上两个函数合并
def printTree(tree):
    a = treeArray(tree)
    if len(a) < 5:
        toTree3(a)
    else:
        print('1')
        toTree4(a)

#
# def isSymmetric1(root):
#     """
#     :type root: TreeNode
#     :rtype: bool
#     """
#
#     def helper(root, mirror):
#         if not root and not mirror:
#             return True
#         if root and mirror and root.val == mirror.val:
#             return helper(root.left, mirror.right) and helper(root.right, mirror.left)
#         return False
#
#     return helper(root, root)
#
#
# def isSymmetric2(root):
#     def isSame(p, q):
#         if p and q and p.val == q.val:
#             return isSame(p.left, q.right) and isSame(p.right, q.left)
#         if not p:
#             return not q
#         return False
#
#     if not root:
#         return True
#     return isSame(root.left, root.right)


if __name__ == '__main__':

    a = [i for i in range(100)]

    t1 = listcreattree(None, a, 0)
    printTree(t1)
    # print(isSymmetric2(t1))

