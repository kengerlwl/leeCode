import math
import copy

import math
import copy
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s= '{}'
        def getS(s, count = len(nums) -1):  # 一共count +1 个参数
            if count ==0:
                return s
            else:
                return '('  +getS(s, count-1)+' / {})'

        s = getS(s)
        # print(s.format())



        arr = nums
        visit = [True for i in range(len(arr))]
        temp = ["" for x in range(0, len(arr))]
        # 回溯记录
        self.ans = -float("INF")
        def dfs(position):
            if position == len(arr):
                # print(temp)
                ts  = s.format(*temp)
                print(ts,eval(ts))
                self.ans  = max(eval(s.format(*temp)), self.ans)
                return

            for index in range(0, len(arr)):
                if visit[index] == True:
                    temp[position] = arr[index]
                    visit[index] = False
                    dfs(position + 1)
                    visit[index] = True


        dfs(0)
        return self.ans







#
# class Solution(object):
#     def optimalDivision(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: str
#         """
#         def getAns(nums):
#             values = []
#             if len(nums) == 2:
#                 return nums[0] / nums[1]
#             if len(nums) == 1:
#                 return nums[0]
#             for i in range(len(nums) -1):
#                 new = copy.deepcopy(nums)
#                 a = nums[i]
#                 b = nums[i+1]
#                 # new.__delitem__(i)
#                 new.__delitem__(i+1)
#                 new[i] = a / b
#
#                 values.append(getAns(new))
#
#             return max(values)
#
#         ans = getAns(nums)
#         print(ans)
#         return ans



# Solution.optimalDivision()
a = Solution()
b= a.optimalDivision([1000,100,10,2])
print(b)