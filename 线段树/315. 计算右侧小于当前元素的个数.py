class Node():
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        self.mid = (begin + end) // 2
        self.count = 0
        self.left = None
        self.right = None

    def add(self, num):
        # 返回线段树中比num小的值的数量
        self.count += 1
        if self.begin == self.end:
            return 0
        else:
            if not self.left:
                self.left = Node(self.begin, self.mid)
            if not self.right:
                self.right = Node(self.mid + 1, self.end)
            if num <= self.mid:
                return self.left.add(num)
            else:
                return self.left.count + self.right.add(num)


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        mn = min(nums)
        mx = max(nums)
        root = Node(mn, mx)
        res = []
        # 这里倒着计算，返回数组前面比自己小的个数
        for i in range(len(nums) - 1, -1, -1):
            # 一边构建线段树一边计算答案
            res.append(root.add(nums[i]))
        return res[::-1]


