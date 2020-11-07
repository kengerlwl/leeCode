#需要对数组的元素进行修改，并查询区间范围内的和。

class BinaryIndexTree:

    def __init__(self, array: list):
        '''初始化，总时间 O(n)'''
        self._array = [0] + array
        n = len(array)
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1:
                self._array[j] += self._array[i]

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, val: int):
        '''将原数组idx下标更新为val, 总时间O(log n)'''
        prev = self.query(idx, idx + 1)    # 计算出原来的值
        idx += 1
        val -= prev    # val 是要增加的值
        while idx < len(self._array):
            self._array[idx] += val
            idx += self.lowbit(idx)

    def query(self, begin: int, end: int) -> int:
        '''返回数组[begin, end) 的和'''
        return self._query(end) - self._query(begin)

    def _query(self, idx: int) -> int:
        '''计算数组[0, idx)的元素之和'''
        res = 0
        while idx > 0:
            res += self._array[idx]
            idx -= self.lowbit(idx)
        return res




if __name__ == '__main__':
    bT = BinaryIndexTree([0,2,1,4,5,4,7,3])
    bT.update(0, 9)
    a = bT.query(0, 1)
    print(a)