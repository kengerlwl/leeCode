
# 可以自定义比较函数，决定排序方式
def cmp(a,b):
    return a>b


class quiteSort:
    def __init__(self):
        self.cmp = lambda a, b:a< b

    # 设置比较函数
    def setCmp(self, cmp):
        self.cmp =cmp

    # 随机找一个中间基准值，将数据分成左右两堆
    def randomized_partition(self, nums, l, r):
        import random
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if self.cmp(nums[j],nums[r]):
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    # 不断进行细分
    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums
