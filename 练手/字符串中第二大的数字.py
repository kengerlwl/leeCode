class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}

        for i in s:
            if i.isdigit():
                if i in count:
                    count[i]+=1
                else:
                    count[i] =1
        ans = []

        for i in count:
                ans.append(i)
        if len(ans) == 0 or len(ans) ==1:
            return -1
        else:
            return sorted(ans)[len(ans)-2]

a = Solution.secondHighest(None, '111')
print(a)