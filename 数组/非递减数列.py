from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified_cnt = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if modified_cnt:
                    return False
                else:
                    if i - 2 >= 0:
                        if nums[i - 2] <= nums[i]:
                            nums[i - 1] = nums[i]
                        else:
                            nums[i] = nums[i - 1]
                    else:
                        nums[i - 1] = nums[i]
                    modified_cnt += 1
        return True

if __name__ == "__main__":
    ans  = Solution.checkPossibility(None,[2,3,1])
    print(ans)