class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        if len(word1) !=len(word2):
            return False


        def getCharSet(s):
            ans ={}
            for i in s:
                if i in ans:
                    ans[i] +=1
                else:
                    ans[i] =1

            return ans

        a = getCharSet(word2)
        b =getCharSet(word1)
        # print(a, b)
        # print([a.values()])
        index_a = sorted(a)
        index_b = sorted(b)







        if index_a == index_b:
            valueA = sorted([a[i] for i in index_a])
            valueB = sorted([b[i] for i in index_b])



            if valueA ==valueB:
                return True
            return False
            # print('True')
        else:
            return False

print(Solution.closeStrings(None,word1 = "cabbba", word2 = "abbccc"))