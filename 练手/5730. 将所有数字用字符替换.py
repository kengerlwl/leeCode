S = 'abcdefghijklmnopqrstuvwxyz'

class Solution(object):
    def __init__(self):
        S = 'abcdefghijklmnopqrstuvwxyz'
        self.S = S
        f= {}
        for i in range(len(S)):
            f[S[i]] = i
        self.f= f

    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        length  = len(s)
        ans = ''
        for i in range(length//2):
            index = i * 2
            char = s[index]
            dis = s[index+1]

            ne = self.f[char] + int(dis)
            # print(self.S[ne])
            #
            #
            # print(s[index])
            ans += s[index] + self.S[ne]

        try:
            int(s[length-1])
        except Exception:
            ans +=s[length-1]
        print(ans)

        return ans

a = Solution()
a.replaceDigits(s = "a1b2c3d4e")