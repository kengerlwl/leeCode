class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        hashSet ={}
        for i in nums:
            if i in hashSet:
                hashSet[i]+=1
            else:
                hashSet[i] =1
        #print(hashSet)

        newHash={}

        for i in hashSet:
            tmpNum = hashSet[i]
            if tmpNum not  in newHash:
                newHash[tmpNum] = [i]
            else:
                newHash[tmpNum].append(i)
        newHashx = sorted(newHash)

        #print(newHash)
        ans =[]
        for i in  newHashx:
            num = newHash[i]
            num.sort()
            num.reverse()
            print(num)
            print()

            for j in num:
                ans+= [j for m in range(hashSet[j])]
        print(ans)
        return ans






Solution.frequencySort(None,[1,1,2,2,2,3])