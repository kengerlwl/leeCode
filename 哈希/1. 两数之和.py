#哈希表的查询时间为 O(1)，算法的时间复杂度降低到 O(N)，但是需要 O(N) 的空间复杂度来存储哈希表
#所以使用哈希的查询
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for index in range(len(nums)):
            hashTable[nums[index]] = index

        for i in range(len(nums)):
            other = target - nums[i]

            if other in hashTable and hashTable.get(other) != i:
                return [i, hashTable.get(other)]
        return []

print(Solution.twoSum(None,nums = [2, 7, 11, 15], target = 9))