
Mod = 10**9+7

class DichotomousSearch():
    def __init__(self):
        pass


    # 查找k在有序数组nums 中得位置。 nums是升序得
    #return index, flag flag是代表是否有和k匹配得数得bool。  这里
    def search(self, nums, k,r):
        l = 0
        r = r

        while l<r:
            mid = (l + r) // 2

            if nums[mid]> k:   #  向左边找
                r = mid - 1
            elif nums[mid] <k:  # 向右边找
                l = mid +1
            elif nums[mid] == k:
                l = mid +1


        if nums[l] == k:
            return l, True
        else:
            return l, False
d= DichotomousSearch()

def find(index,nums, tar):
    # print(tar)
    n, f = d.search(nums, tar,r=index)
    # print(n, f)
    if f:
        while nums[n] <= tar and n <= index:
            n+=1
        if n> index:
            n = index+1

        return n
    else:
        while nums[n] <= tar and n <= index:
            n+=1
        if n> index:
            n = index+1
        return  n




class Solution(object):
    def purchasePlans(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        ans = 0
        for i in range(1, length):
            index =find(i-1, nums, target- nums[i])
            # print(index)
            ans+= index

        print(ans)
        return ans % Mod


Solution.purchasePlans(None,nums = [1,1,1,1,1,1], target = 6)
