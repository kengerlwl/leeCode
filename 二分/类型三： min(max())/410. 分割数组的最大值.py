class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def check(maxV): # 当和为mid能不能满足
            ans =0
            curS =0
            for i in nums:
                if i > maxV:
                    return False
                if curS + i > maxV: #超过了最大限制
                    curS = i
                    ans +=1
                else:
                    curS +=i
            if curS > 0:
                ans +=1

            # print(ans)
            if ans <= m:
                return True
            else:
                return False

        # print(check(1))
        # return 0
        l = 1
        r = 500000000
        import  math
        while l < r:
            mid = math.floor((l + r)/2)
            # print(l,r, mid)
            if check(mid):
                r = mid
            else:
                l = mid+1

        print(l, r)
        return int(l)




Solution.splitArray(None,[5,1,3,5,10,7,4,9,2,8],
1)