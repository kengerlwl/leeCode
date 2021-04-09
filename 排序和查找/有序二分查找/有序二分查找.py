class DichotomousSearch():
    def __init__(self):
        pass


    # 查找k在有序数组nums 中得位置。 nums是升序得
    #return index, flag flag是代表是否有和k匹配得数得bool。这里没有考虑数组中有很多相同的元素
    def search(self, nums, k):
        l = 0
        r = len(nums)-1

        while l<=r:



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





d = DichotomousSearch()

print(d.search(
[1,9, 9,9,9,11,11,11,16],
9

)

)