class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import copy

        sumSet ={}


        curSum = {
            'a':0,
            'e':0,
            'i':0,
            'o':0,
            'u':0
        }


        def tostate(stateSet):
            result = ''
            for i in stateSet:
                result += str(stateSet[i])
            return result

        sumSet[tostate(curSum)] = -1


        count =0
        maxV = 0
        for i in s:
            if i in curSum:
                curSum[i] +=1
                curSum[i] = curSum[i] % 2


            # print(tostate(curSum))
            if tostate(curSum) in sumSet:
                dis = count - sumSet[tostate(curSum)]
                # print(dis)
                if dis > maxV:
                    maxV = dis
            else:
                sumSet[tostate(curSum)] = count
            count +=1

        return maxV

Solution.findTheLongestSubstring(None,"leetcodeisgreat")
