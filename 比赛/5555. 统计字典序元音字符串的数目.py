class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        charMap = {
            'a':5,
            'e':4,
            'i':3,
            'o':2,
            'u':1
        }
        charMapOne = {
            'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1
        }
        charMapZero = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }
        index = sorted(charMap)
        # print(index)
        import copy
        def dg(n):

            if n ==1:
                return charMapOne


            charSet = dg(n-1)
            newCharMap =copy.deepcopy(charMapZero)

            for i in index:

                tmpnum = charSet[i]  # 字符a数目
                for j in range(5- charMap[i], 5):
                    newCharMap[index[j]] += charSet[i]

            return newCharMap

        ans = dg(n)
        print(ans)
        count =0
        for i in ans:
            count += ans[i]
        print(count)
        return count


Solution.countVowelStrings(None, 33)