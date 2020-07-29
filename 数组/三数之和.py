# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针
#  👍 2426 👎 0

#主要先进行排序预处理，然后通过指针进行遍历，
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num = sorted(nums)
        length = len(nums)
        # print(num)
        res = []
        for ix,i in enumerate(num):
            if ix >= length-2:
                continue
            if i == num[ix -1] and ix > 0:
                continue
            print(num)
            target = 0- i
            left = ix +1
            right =  length -1

            while left < right:
                s = num[left] + num[right]
                if s == target:
                    res.append([i, num[left], num[right]])
                    print(ix, res)
                    print(left, right)
                    print(num[left] ,num[right])
                    left +=1
                    right -=1
                    while left<right and num[left] == num[left-1]:  # 跳过重复的要和走过的比
                                            left += 1
                    while left<right and num[right] == num[right+1]:
                                            right -= 1

                elif s < target:
                    left +=1
                else:
                    right -=1

        print(res)
        return res








# leetcode submit region end(Prohibit modification and deletion)
Solution.threeSum(None, [-1,0,1,2,-1,-4])
