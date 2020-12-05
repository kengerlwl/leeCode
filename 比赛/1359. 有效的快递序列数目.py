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
    return math.factorial(n)//math.factorial(n-m)                        #使用自己的阶乘函数计算排列数


class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """

        def getAns(n):
            if n ==1:
                return 1
            else:
                last = getAns(n-1)
                num = (n-1) *2

                new = comb_1(num+1,2) + num +1

                return (last * new) % (10**9+7)

        ans  = getAns(n)
        print(ans)
        return ans


Solution.countOrders(None,3)
