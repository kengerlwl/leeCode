class Solution:
    def letterCombinations(self, digits) :
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }


        ans =[]
        leng = len(digits)
        end = digits[leng-1]
        print(end)
        def back(start,s):

            if start == leng:
                ans.append(s)
                return

            N = digits[start]
            listOfN = phoneMap[N]

            for i in listOfN:

                back(start+1, s + i)

        back(0, '')

        print(ans)
        return ans


Solution.letterCombinations(None,'235')
