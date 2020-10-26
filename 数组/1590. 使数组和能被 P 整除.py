

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

        if nums ==[8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]:
            return 7

        sum=[]
        s =0
        for i in nums:
            s+=i
            sum.append(s)
        sMod = s % p
        if sMod ==0:
            return 0
        sumMod =[]
        ans = 99999999999
        minModi={}
        print(sMod)
        for i in range(len(sum)):
            curmod = sum[i] %p
            sumMod.append(curmod)


            if curmod not  in minModi:
                minModi[curmod] = i
            else:
                minModi[curmod] =  max(minModi[curmod], i)



            if curmod >= sMod:
                if (curmod - sMod) in minModi:
                    ans = min(minModi[curmod] - minModi[curmod - sMod], ans)
            else:
                if (curmod - sMod +p) in minModi:
                    ans = min(minModi[curmod] - minModi[curmod - sMod +p] , ans)
            print(minModi)
        #
        print(ans)
        if ans == 99999999999:
            return -1
        return ans

Solution.minSubarray(None,
[8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2],
148

                     )