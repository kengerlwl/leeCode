class DichotomousSearch():
    def __init__(self):
        pass


    # 查找k在有序数组nums 中得位置。 nums是升序得
    #return index, flag flag是代表是否有和k匹配得数得bool。
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
        else:
            return l, False





d = DichotomousSearch()

print(d.search(
[9, 16],
5

)

)