# 最大堆的实现
class MaxHeap():
    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.li = [None] * maxSize
        self.count = 0

    def length(self):
        # 求数组的长度
        return self.count

    def show(self):
        if self.count <= 0:
            print('null')
        else:
            print(self.li[: self.count])

    def add(self, value):
        if self.count >= self.maxSize:  # 判断是否数组越界
            raise Exception('full')

        self.li[self.count] = value  # 将新节点增加到最后
        self._shift_up(self.count)  # 递归构建大堆
        self.count += 1

    def _shift_up(self, index):
        # 往大堆中添加元素，并保证根节点是最大的值:
        # 1.增加新的值到最后一个结点，在add实现； 2.与父节点比较，如果比父节点值大，则交换
        if index > 0:
            parent = (index - 1) // 2  # 找到根节点
            if self.li[index] > self.li[parent]:  # 交换结点
                self.li[index], self.li[parent] = self.li[parent], self.li[index]
                self._shift_up(parent)  # 继续递归从底往上判断

    def extract(self):
        # 弹出最大堆的根节点，即最大值
        # 1.删除根结点，将最后一个结点作为更结点 ； 2.判断根结点与左右结点的大小，交换左右结点较大的
        if not self.count:
            raise Exception('null')
        value = self.li[0]
        self.count -= 1
        self.li[0] = self.li[self.count]  # 将最后一个值变为第一个
        self._shift_down(0)
        return value

    def _shift_down(self, index):
        # 1.判断是否有左子节点并左大于根，左大于右；2.判断是否有右子节点，右大于根
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        # 判断条件


        # 下面2个条件包含了，判断左右结点那个大的情况。如果为3， 4， 5,：
        #第一个判断条件使得largest = 1，再执行第二个条件，则判断其左结点与右结点的大小
        if left < self.length() and self.li[left] > self.li[largest]:
            largest = left
        if right < self.length() and self.li[right] > self.li[largest]:
            largest = right

        if largest != index:  # 将 两者交换
            self.li[index], self.li[largest] = self.li[largest], self.li[index]
            self._shift_down(largest)

m = MaxHeap(10)
import numpy as np

np.random.seed(123)
num = np.random.randint(100, size=10)  # 创建随机的10个数
print(m.length())
for i in num:
    m.add(i)
    m.show()
m.show()
print(m.length())

for i in range(5):
    print(m.extract(), end=' ,')

m.show()