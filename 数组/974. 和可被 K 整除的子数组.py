class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        l = len(A)
        sum = [0] * (l+1 )
        sum[0] =0
        for ix, i in enumerate(A):

            sum[ix+1] = sum[ix ] + i
        count =0

        #注意使用同余定理进行计算
        print(sum)

        record = [0] * K
        for i in sum:
            record[i % K] += 1  # 余数为0比较特殊，要把单独可以为0得算进去，也就是本身就是5得倍数得那种。
        ans =0
        print(record)
        for i in record:
            ans += i*(i-1)//2
        return ans
        #传统得穷举得办法
        # for i in range(0, l):
        #     j =i+1
        #
        #     if sum[i] % K ==0:
        #         count = count +1
        #
        #     while(j < l):
        #         tmp = sum[j] - sum[i]
        #         if tmp % K ==0:
        #             count = count +1
        #         j = j +1
        #
        # return count





ans = Solution.subarraysDivByK(None, A = [4,5,0,-2,-3,1], K = 5)
print(ans)