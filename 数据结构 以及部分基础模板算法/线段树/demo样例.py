class SegmentTree:
    """线段树类"""

    def __init__(self, alist, merger_):
        """
        Description: 线段树的构造函数
        Params:
        - alist: 用户传入的一个list（这里我们就不用以前实现的Arr类了，直接用python的list啦，如果想用的话也是一点问题都没有的～）
        - func: merge函数，用于对实现两个数合成一个数的功能（比如二元操作符加法、乘法……等等）
        """
        self._data = alist[:]  # 所以为了不改变传入的数组，需要传其副本
        self._tree = [None] * 4 * len(self._data)  # 注意是4倍的存储空间，初始化元素全是None
        # self._tree = [None for i in range(len(self._data) * 4)]
        self._merger = merger_  # merger函数，比如两个元素求和函数……，用lambda表达式比较方便

        self._buildSegmentTree(0, 0, len(self._data) - 1)  # 调用self._buildSegmentTree来构建线段树

    def getSize(self):
        """
        Description: 获取有效元素的个数
        Returns:
        有效元素个数
        """
        return len(self._data)

    def get(self, index):
        """
        Description: 根据索引index获取相应元素
        时间复杂度：O(1)
        Params:
        - index: 传入的索引
        Returns:
        index索引处的元素值
        """
        if index < 0 or index >= len(self._data):
            raise Exception('Index is illegal!')
        return self._data[index]

    def query(self, quaryL, quaryR):
        """
        Description: 查找[quaryL, quaryR]这个左闭右闭区间上的值（例如对于求和操作就是求这个区间上所有元素的和）
        时间复杂度：O(logn)
        Params:
        - quaryL: 区间左端点的索引
        - quaryR: 区间右端点的索引
        Returns:
        [quaryL, quaryR]区间上的值
        """
        if quaryL < 0 or quaryR < 0 or quaryL >= self.getSize() or quaryR >= self.getSize() or quaryR < quaryL:  # 索引合法性检查
            raise Exception('The indexes is illegal!')
        return self._query(0, 0, self.getSize() - 1, quaryL, quaryR)  # 调用self._quary函数

    def set(self, index, e):
        """
        Description: 将数组中index位置的元素设为e，因此此时需要对线段树的内容要进行更新操作(也就是线段树的更新操作)
        时间复杂度：O(logn)
        Params:
        - index: 数组中的索引
        - e: 索引index上元素的新值e
        """
        if index < 0 or index >= self.getSize():
            raise Exception('The index is illegal!')
        self._data[index] = e  # 更新self._data
        self._set(0, 0, len(self._data) - 1, index, e)  # 调用self._set函数

    def printSegmentTree(self):
        """对线段树进行打印"""
        print('[', end=' ')
        for i in range(len(self._tree)):
            if i == len(self._tree) - 1:
                print(self._tree[i], end=' ]')
                break
            print(self._tree[i], end=',')

    # private
    def _leftChild(self, index):
        """
        Description: 和最大堆一样，由于线段树是一颗完全二叉树，所以可以通过索引的方式找到其左、右孩子的索引（元素从索引0开始盛放）
        Params:
        - index: 输入的索引
        Returns:
        左孩子的索引值
        """
        return 2 * index + 1  # 一定要记住线段树是一棵满树哦，所以用数组就能表示这棵树了，索引关系也和堆是一样的，只不过不需要求父亲节点的索引了

    def _rightChild(self, index):
        """
        Description: 和最大堆一样，由于线段树是一颗完全二叉树，所以可以通过索引的方式找到其左、右孩子的索引（元素从索引0开始盛放）
        Params:
        - index: 输入的索引
        Returns:
        右孩子的索引值
        """
        return 2 * index + 2

    def _buildSegmentTree(self, treeIndex, left, right):
        """
        Description: 以根节点索引为treeIndex，构造self._data索引在[left, right]上的线段树
        Params:
        - treeIndex: 线段树根节点的索引
        - left: 数据左边的索引
        - right: 数据右边的索引
        """
        if left == right:  # 递归到底的情况，left == right，此时只有一个元素
            self._tree[treeIndex] = self._data[left]  # 相应的，self._tree上索引为treeIndex的位置的值置为self._data[left]就好
            return

        leftChild_index = self._leftChild(treeIndex)  # 获取左孩子的索引
        rightChild_index = self._rightChild(treeIndex)  # 获取右孩子的索引

        mid = left + (right - left) // 2  # 获取left和right的中间值，在python中，可以用(left + right) // 2的方式来获得mid，因为不存在数值越界问题
        self._buildSegmentTree(leftChild_index, left, mid)  # 递归向左孩子为根的左子树构建线段树
        self._buildSegmentTree(rightChild_index, mid + 1, right)  # 递归向右孩子为的右子树构建线段树
        self._tree[treeIndex] = self._merger(self._tree[leftChild_index], self._tree[
            rightChild_index])  # 在回归的过程中，用self._merger函数对两个子节点的值进行merger操作，从而完成整棵树的建立

    def _query(self, treeIndex, left, right, quaryL, quaryR):
        """
        Description: 在根节点索引为treeindex的线段树上查找索引范围为[quaryL, quaryR]上的值，其中left， right值代表该节点所表示的索引范围（左闭右闭）
        Params:
        - treeIndex: 根节点所在的索引
        - left: 根节点所代表的区间的左端的索引值(注意是左闭右闭区间哦)
        - right: 根节点所代表的区间的右端点的索引值
        - quaryL: 待查询区间的左端的索引值（也是左闭右闭区间）
        - quaryR: 待查询区间的右端的索引值
        """
        if left == quaryL and right == quaryR:  # 递归到底的情况，区间都对上了，直接返回当前treeIndex索引处的值就好
            return self._tree[treeIndex]  # 返回当前树上索引为treeIndex的元素值

        mid = left + (right - left) // 2  # 获取TreeIndex索引处所代表的范围的中点
        leftChild_index = self._leftChild(treeIndex)  # 获取左孩子的索引
        rightChild_index = self._rightChild(treeIndex)  # 获取右孩子的索引

        if quaryL > mid:  # 此时要查询的区间完全位于当前treeIndex所带表的区间的右侧
            return self._query(rightChild_index, mid + 1, right, quaryL, quaryR)  # 直接去右子树找[quaryL, quaryR]
        elif quaryR <= mid:  # 此时要查询的区间完全位于当前treIndex所代表的区间的左侧
            return self._query(leftChild_index, left, mid, quaryL, quaryR)  # 直接去左子树找[quaryL, quaryR]

        # 此时一部分在[left, mid]上，一部分在[mid + 1, right]上
        leftResult = self._query(leftChild_index, left, mid, quaryL, mid)  # 在左子树找区间[quaryL, mid]
        rightResult = self._query(rightChild_index, mid + 1, right, mid + 1, quaryR)  # 在右子树找区间[mid + 1, quaryR]
        return self._merger(leftResult, rightResult)  # 最后在回归的过程中两个子节点进行merger操作并返回,得到[quaryL, quaryR]区间上的值

    def _set(self, treeIndex, left, right, index, e):
        """
        Description: 在以索引treeIndex为根节点的线段树中将索引为index的位置的元素设为e（此时treeIndex索引处所代表的区间范围为：[left, right]
        params:
        - treeIndex: 传入的线段树的根节点索引值
        - left: 根节点所代表的区间的左端的索引值
        - right: 根节点所代表的区间的右端点的索引值
        - index: 输入的索引值
        - e: 新的元素值
        """
        if left == right:  # 递归到底的情况，也就是在树中找到了索引为index的元素
            self._tree[treeIndex] = e  # 直接替换
            return

        mid = left + (right - left) // 2  # 找到索引中间值
        leftChild_index = self._leftChild(treeIndex)  # 左孩子索引值
        rightChild_index = self._rightChild(treeIndex)  # 右孩子索引值

        if index <= mid:  # index处于当前treeIndex所代表的区间的左半区
            self._set(leftChild_index, left, mid, index, e)  # 到左子树去找index
        else:  # 否则index处于当前treeIndex所代表的区间的右半区
            self._set(rightChild_index, mid + 1, right, index, e)  # 到右子树去找index
        self._tree[treeIndex] = self._merger(self._tree[leftChild_index], self._tree[
            rightChild_index])  # 由于对树的最底层元素进行了更新操作，因此需要对树的上层也进行一次更新，所以每次回归的都调用merger操作进行上层的值的更新操作


if __name__ == '__main__':
    input_list = [-2, 0, 3, -5, 2, -1]
    test_st = SegmentTree(input_list, merger_=lambda x, y: x + y)  # 这里以求和为例
    test_st.printSegmentTree()
    print()
    print('索引区间[0, 4]上的元素的和为：', test_st.query(0, 4))
    print('将索引为0的元素置为10：')
    test_st.set(0, 10)
    test_st.printSegmentTree()

    print('\n此时索引区间[0, 4]上的元素的和为：', test_st.query(0, 4))