class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ans = 0
        ct = CountTree(1, 100000, 10)
        for v in instructions:
            l, r = ct.getBigLessCount(v)
            if l <= r:
                ans += l
            else:
                ans += r
            ans %= 1000000007
            ct.put(v)
        return ans


class CountTree(object):
    def __init__(self, minValue: int, maxValue: int, bktSize: int):
        self.__minValue = minValue
        self.__maxValue = maxValue
        self.__bktSize = bktSize
        self.__mask = 1
        maxSize = maxValue - minValue
        while self.__mask * bktSize <= maxSize:
            self.__mask *= bktSize
        self.__root = CountNode(bktSize, self.__mask)

    def put(self, value: int):
        self.__root.put(value - self.__minValue)

    def getBigLessCount(self, value: int):
        return self.__root.getBigLessCount(value - self.__minValue)


class CountNode(object):
    def __init__(self, blkSize: int, mask: int, value=None):
        self.__value = value
        self.__mask = mask
        self.__cnts = [0] * blkSize
        self.__next = None

    def put(self, value: int, cnt: int = 1):
        bktSize = len(self.__cnts)
        idx = int((value / self.__mask) % bktSize)
        if self.__mask == 1:
            self.__cnts[idx] += cnt
            if self.__value != value:
                self.__value = None
            return

        if self.__value is not None:
            if self.__value == value:
                self.__cnts[idx] += cnt
                return
            cidx = int((self.__value / self.__mask) % bktSize)
            self.__next = [None] * bktSize
            self.__next[cidx] = CountNode(bktSize, int(self.__mask / bktSize), self.__value)
            self.__next[cidx].put(self.__value, self.__cnts[cidx])
            self.__value = None

        if not self.__next:
            self.__next = [None] * bktSize

        self.__cnts[idx] += cnt
        if not self.__next[idx]:
            self.__next[idx] = CountNode(bktSize, int(self.__mask / bktSize), value)
        self.__next[idx].put(value, cnt)

    def getBigLessCount(self, value: int):
        idx = int((value / self.__mask) % len(self.__cnts))
        if self.__value is not None:
            if value == self.__value:
                return 0, 0
            cidx = int((self.__value / self.__mask) % len(self.__cnts))
            if value < self.__value:
                return 0, self.__cnts[cidx]
            return self.__cnts[cidx], 0

        l, r = 0, 0
        for i in range(idx):
            l += self.__cnts[i]
        for i in range(idx + 1, len(self.__cnts)):
            r += self.__cnts[i]
        if self.__next and self.__next[idx]:
            cl, cr = self.__next[idx].getBigLessCount(value)
            l += cl
            r += cr
        return l, r
