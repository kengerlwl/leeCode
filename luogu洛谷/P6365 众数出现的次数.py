
# 可以自定义比较函数，决定排序方式
def cmp(a,b):
    if a[0] > b[0]:
        return True
    elif a[0] == b[0] and a[1] <b[1]:
        return True
    else:
        return False


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



n = input()
n= int(n)

cards = []
count= {}
counts = []
for i in range(n):
    s = input().split(' ')
    a = s[0]
    b= s[1]
    a = int(a)
    b= int(b)

    cards.append([a, a^b])
    if a in count:
        count[a] +=1
    else:
        count[a] =1

    b = a^b
    if b in count:
        count[b] +=1
    else:
        count[b] =1

for i in count:
    counts.append([count[i], i])

q = quiteSort()
q.setCmp(cmp=cmp)

counts = q.sortArray(counts)
# print(counts)
#
#
# print(cards)

def jusge(num):
    ans =0
    for a, b in cards:
        if a == num or b ==num:
            ans +=1

    return ans


for nums, num in counts:
    if nums <= jusge(num):
        print(num)
        break