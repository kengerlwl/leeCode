class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        left = [0] * (l+1)
        right = [0] * (l +1)
        Lset = set()
        Rset  = set()
        for i in range(1, l +1):
            # left
            Lset.add(s[i-1])
            left[i] = len(Lset)

            #right
            Rset.add(s[l-i])
            right[l-i +1] = len(Rset)



        ans = 0
        for i in range(1, l):
            if left[i] == right[i+1]:
                ans+=1

        # print(ans)

        # print(left, right)
        return  ans




Solution.numSplits(None,"acbadbaada")