

class Solution(object):
    count = 0

    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """


        def getmin(l, r):
            # print(l ,r)



            if l > r:
                return 0

            if l == r:
                Solution.count += target[l]

                return target[l]

            getZero = True
            tmp = 0

            while(getZero):

                flag = True
                for i in range(l, r+1):
                    if target[i] == 0:
                        flag = False
                if flag:
                    for i in range(l, r + 1):
                        target[i] -=1
                    Solution.count +=1
                    tmp +=1


                for i in range(l, r + 1):
                    if target[i] == 0:
                        return getmin(l, i-1)+getmin(i+1, r) + tmp
                        getZero = False
                        break

        length = len(target)
        ans =  getmin(0, length-1)
        # print(ans)
        # print(Solution.count)
        return ans




Solution.minNumberOperations(None,[3,1,5,4,2])