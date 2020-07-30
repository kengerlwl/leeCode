class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l <=r:
            # print(l, r)
            mid = (l+r)//2

            #向左
            flag = True
            while flag:
                if nums[mid] ==mid:
                    return mid

                if nums[mid] == nums[mid-1] and mid >=1 and mid >l:
                    mid -=1
                else:
                    flag =False

            # 向右
            flag = True
            while flag:
                if nums[mid] ==mid:
                    return mid

                if nums[mid] == nums[mid+1]  and mid < r:
                    mid +=1
                else:
                    flag =False



            if nums[mid] > mid:
                r = mid-1
            elif nums[mid] < mid:
                l = mid+1
            else:
                return mid
        return  -1




ans = Solution.findMagicIndex(None,[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32])
print(ans)