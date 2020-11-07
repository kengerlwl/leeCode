class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        cur =1
        nJC ={}
        import copy
        for i in range(1, n+1):
            cur *= i
            nJC[i] =cur
        print(nJC)
        import math

        select = [i for i in range(1,n+1)]

        def dg(n, k, select):

            print('this time is: ', n, k, select)
            if n ==1 and k ==1:
                return select[0]
            if n ==2 and k == 1:
                return str(select[0]) + str(select[1])
            if n==2 and k ==2:
                return str(select[1]) + str(select[0])

            thisSele =None
            if k <= nJC[n-1]:
                thisSele = 1
            else:
                thisSele = math.ceil(k / (nJC[n-1]))  # 向上取整

            print(thisSele)
            thisnum = select[thisSele -1]
            knew = None
            if k <= nJC[n-1]:
                knew = k
            else:
                knew = k - (thisSele -1) * nJC[n-1]
                print('knew',knew)

            nextSelect = copy.deepcopy(select)
            nextSelect.remove(thisnum)

            return str(thisnum) + str(dg(n-1, knew, nextSelect))

        ans  = dg(n, k, select)
        print(ans)
        return str(ans)
Solution.getPermutation(None, 3,3)



