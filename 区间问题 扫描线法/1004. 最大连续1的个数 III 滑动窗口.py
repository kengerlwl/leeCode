class Solution(object):
    def longestOnes(self, A, K):
        N = len(A)
        res = 0
        left, right = 0, 0
        zeros = 0
        while right < N:
            if A[right] == 0:
                zeros += 1
            while zeros > K:
                if A[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)

            right += 1
        return res
