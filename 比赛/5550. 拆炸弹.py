class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        length = len(code)

        def getNumFromCode(i):

            if i <0:
                i += 100 * length
                return code[i % length]

            elif 0<=i and i< length:
                return code[i]
            else:
                return code[i % length]
        ans =[]


        if k ==0:
            return [0 for i in range(length)]
        elif k >0:
            for i in range(length):
                tmpSum =0
                for j in range(1,k+1):
                    tmpSum += getNumFromCode(i+j)
                ans.append(tmpSum)
        elif k <0:
            for i in range(length):
                tmpSum =0
                for j in range(1,(-1)*k+1):
                    tmpSum += getNumFromCode(i-j)
                ans.append(tmpSum)


        # print(ans)
        return ans

Solution.decrypt(None, code = [2,4,9,3], k = -2)

