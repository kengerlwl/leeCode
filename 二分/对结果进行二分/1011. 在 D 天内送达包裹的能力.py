class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """

        def check(num):
            curS =0
            ans = 0
            for i in weights:

                if i > num:  
                    return False

                if curS + i > num:
                    ans +=1
                    # print(curS)
                    curS =i
                else:
                    curS += i

            # print(curS)
            if curS > 0:
                ans+=1


            if ans > D:
                 return False  # 一个不够大的值
            else:
                 return True    # 一个不够大的值

        # return 0

        l =1
        r = sum(weights)
        while l < r:
            mid = (l + r)//2
            # print(l,r, mid)

            if check(mid):
                r = mid
            else:
                l = mid +1

        print(l, r)
        return r


Solution.shipWithinDays(None,[1,2,3,1,1],
4)