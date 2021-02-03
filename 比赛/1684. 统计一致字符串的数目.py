class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        f = {}
        for i in allowed:
            f[i] = True

        count  =0
        for i in words:
            flag = True
            for char in i:
                if char not in f:
                    flag = False
                    break

            if flag :
                count +=1

        print(count)
        return count

Solution.countConsistentStrings(None,allowed = "ab", words = ["ad","bd","aaab","baa","badab"])