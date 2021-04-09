import math

class DichotomousSearchRight():  # 向右边找
    def __init__(self):
        pass

    # 查找k在有序数组nums 中得位置。 nums是升序得
    #return index, flag flag是代表是否有和k匹配得数得bool。这里没有考虑数组中有很多相同的元素
    def search(self, nums, k):
        l = 0
        r = len(nums)-1# 取右边

        while l<r:
            mid =math.ceil((l + r) / 2)

            if nums[mid]> k:   #  向左边找
                r = mid - 1
            elif nums[mid] <k:  # 向右边找
                l = mid +1
            elif nums[mid] == k:
                l = mid



        if nums[l] == k:
            return l, True
        elif nums[l] >k:
            return l, False
        elif nums[l] < k:
            return l+1, False


class DichotomousSearchLeft():  # 向右边找
    def __init__(self):
        pass


    # 查找k在有序数组nums 中得位置。 nums是升序得
    #return index, flag flag是代表是否有和k匹配得数得bool。这里没有考虑数组中有很多相同的元素
    def search(self, nums, k):
        l = 0
        r = len(nums)-1# 取右边

        while l<r:
            # print(l, r)

            mid =math.floor((l + r) / 2)

            if nums[mid]> k:   #  向左边找
                r = mid - 1
            elif nums[mid] <k:  # 向右边找
                l = mid +1
            elif nums[mid] == k:
                r = mid

        if nums[l] == k:
            return l, True
        elif nums[l] >k:
            return l, False
        elif nums[l] < k:
            return l+1, False



d = DichotomousSearchRight()

print('向右边查找',d.search(
[1,9, 9,9,9,11,11,11,16],
9
)
)



d = DichotomousSearchLeft()

print('向左边查找',d.search(
[1,9, 9,9,9,11,11,11,16],
8

)

)