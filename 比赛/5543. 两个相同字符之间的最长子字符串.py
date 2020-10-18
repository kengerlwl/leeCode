class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans =-1
        for i in range(len(s)):
            for j in  range(i+1, len(s)):
               if s[i] == s[j]:
                ans = max(j-i-1, ans)

        print(ans)





Solution.maxLengthBetweenEqualCharacters(None, "aa")