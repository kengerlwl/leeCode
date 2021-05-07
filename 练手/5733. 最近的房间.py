import random
# 可以自定义比较函数，决定排序方式
def cmp1(a,b):
    if a[1]>b[1]:
        return True
    elif a[1]==b[1]:
        return a[0] < b[0]

    else:
        return False


def cmp2(a,b):
    return a[1]<b[1]

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
        self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

class DichotomousSearch():
    def __init__(self):
        pass


    # 查找k在有序数组nums 中得位置。 nums是升序得
    #return index, flag flag是代表是否有和k匹配得数得bool。这里没有考虑数组中有很多相同的元素
    def search(self, nums, k):
        l = 0
        r = len(nums)-1

        while l<r:



            mid = (l + r) // 2

            if nums[mid]> k:   #  向左边找
                r = mid - 1
            elif nums[mid] <k:  # 向右边找
                l = mid +1
            elif nums[mid] == k:
                l = r = mid
                break


        if nums[l] == k:
            return l, True
        elif nums[l] >k:  # 更小就插入当前位置前面
            return l, False
        elif nums[l] < k:# 向右边插入这个位置
            return l+1, False




import heapq

class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s1= quiteSort()
        s1.setCmp(cmp1)
        rooms = s1.sortArray(rooms)

        for i in range(len(queries)):
            queries[i].append(i)


        queries = s1.sortArray(queries)

        print(rooms, queries)
        k = len(queries)
        ans = []
        queue = []
        queue

        index = 0
        for i in range(k):
            # print('the asdfsadfsadf', i)
            preid, size, j = queries[i]
            # print((size))
            while index < len(rooms) and rooms[index][1] >= size :
                heapq.heappush(queue, rooms[index][0] )
                index+=1
            d = DichotomousSearch()
            if i == 2:
                queue = sorted(queue)
            # print(queue)

            if queue == []:
                ans.append([-1, j])
                continue

            next, flag = d.search(queue, preid)

            # print(next, flag)
            if flag:
                ans.append([queue[next],j])
            else:
                left = None
                right = None
                try:
                    left = queue[next-1]
                    leftD = preid - left
                    # print(left)
                except Exception:
                    pass

                try:
                    right = queue[next]
                    rightD = right - preid
                    # print(left)
                except Exception:
                    pass

                if left and right:
                    if leftD > rightD:
                        ans.append([left, j])
                    elif leftD == rightD:
                        ans.append([left, j])
                    else:
                        ans.append([right, j])
                elif left:
                    ans.append([left, j])
                else:
                    ans.append([right, j])




        print(ans)

        ans = s1.sortArray(ans)
        print(ans)
        F = []
        for i, j in ans:
                F.append(i)
        F.reverse()
        print(F)
        return F







Solution.closestRoom(None,
[[23,22],[6,20],[15,6],[22,19],[2,10],[21,4],[10,18],[16,1],[12,7],[5,22]],
[[12,5],[15,15],[21,6],[15,1],[23,4],[15,11],[1,24],[3,19],[25,8],[18,6]]
                     )
