class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        print(sorted(nums))
        k  = len(nums) - k +1
        ans = None
        #接用快排
        while True:
            bigger = []
            smaller = []
            same = []
            mid = nums[0]
            for i in range(0, len(nums)):  # 将所有的元素分一下
                now = nums[i]
                if now > mid:
                    bigger.append(now)
                elif now < mid:
                    smaller.append(now)
                else:
                    same.append(now)

            if k <= len(smaller):
                nums = smaller
            elif k > len(smaller) + len(same):
                nums = bigger
                k = k - len(smaller) - len(same)
            else:
                ans  = mid
                break

        print(ans)
        return ans


Solution.findKthLargest(None, [3,2,3,1,2,4,5,5,6],
4)