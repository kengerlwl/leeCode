class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        length = len(s)
        for i in range(length):
            c = s[i]

            if c not  in count:
                count[c] = [True, i]
            else:
                count[c] = [False, count[c][1]]

        inf = float('INF')
        ans = inf
        val = None
        for i in count:
            if count[i][0]:  # 只出现了一次
                ans =min(count[i][1], ans)


        if ans == inf:
            return -1
        else:
            return ans