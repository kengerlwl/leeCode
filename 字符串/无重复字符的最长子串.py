# 使用dp，构建状态转移方程

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        if len(s) == 1:
            return 1

        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)
        length = 1;
        for ix , i in enumerate(s):
            length = max(length, find_left(s, ix))
        # print(length)
        return length

Solution.lengthOfLongestSubstring(None, "ansddf")