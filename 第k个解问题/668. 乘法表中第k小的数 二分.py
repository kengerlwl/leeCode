class Solution(object):

    # 计算比k小的个数
    def findKthNumber(self, m, n, k):
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)  #这一步妙啊
            return count >= k


        # 进行二分
        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) / 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

