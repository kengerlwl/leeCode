class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        S1 =[]
        for i in s1:
            S1.append(i)
        S1 = sorted(S1)

        S2 = []
        for i in s2:
            S2.append(i)
        S2 = sorted(S2)

        length = len(s1)
        print(S1)
        print(S2)

        for i in range(length):
            print(S1[i] > S2[i])
            if S1[i] > S2[i]:
                return False
        return True

print(Solution.checkIfCanBreak(None,"szy",
"cid"))