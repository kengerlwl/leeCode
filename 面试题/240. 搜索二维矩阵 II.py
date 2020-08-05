class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 :
            return False
        elif len(matrix[0]) == 0:
            return False

        def getMid(nums, target):
            l = 0
            r = len(nums)-1

            while(l <r):



                mid = (l +r)//2

                if r - l == 1 and(nums[l] < target < nums[r]):
                    return l

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid +1

            return l
        import numpy as np


        # 从行开始遍历
        matrix = np.array(matrix)
        matrix.reshape(len(matrix), -1)
        tmp = matrix[0,:]

        mid = getMid(tmp,target)
        ans = getMid(matrix[:, mid],target)
        for i in range(mid+1):
            ans = getMid(matrix[:, i], target)
            # print(matrix)
            # print(ans, i)
            f  = matrix[ans, i]
            if f == target:
                return True



        matrix =matrix.transpose()
        matrix.reshape(len(matrix), -1)

        tmp = matrix[0,:]
        mid = getMid(tmp,target)
        for i in range(mid+1):
            ans = getMid(matrix[:, i], target)
            # print(matrix)
            # print(ans, i)
            f  = matrix[ans, i]
            if f == target:
                return True


        return False






ans = Solution.searchMatrix(None, [[-1]], -1)
print(ans)