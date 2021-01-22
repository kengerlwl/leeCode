import math

def factorial_(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

def comb_1(n,m):
    return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))  #直接使用math里的阶乘函数计算组合数

def comb_2(n,m):
    return factorial_(n)//(factorial_(n-m)*factorial_(m))              #使用自己的阶乘函数计算组合数

def perm_1(n,m):
    return math.factorial(n)//math.factorial(n-m)                        #直接使用math里的阶乘函数计算排列数

def perm_2(n,m):
    return math.factorial(n)//math.factorial(n-m)

class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        length = len(nums)
        nums = sorted(nums)
        for i in range(length):
            for j in range(i+1,length):
                if i !=j:
                    tmp = nums[i] * nums[j]
                    # print(tmp)
                    if tmp in count:
                        count[tmp] +=1
                    else:
                        count[tmp] = 1

        # print(count)
        ans = 0
        for i in count:
            now  =  count[i]
            if now >=2:
                ans += comb_2(now,2)

        print(ans*8)
        return ans*8
Solution.tupleSameProduct(None,nums = [2,3,5,7])
