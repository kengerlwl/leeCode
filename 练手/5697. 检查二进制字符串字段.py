class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = 0
        flag = False
        ans = s.count('1')

        for i in s:
            if i == '1':
                flag = True
                count +=1
            else:
                if flag:
                    break

        if ans > count:
            return False
        elif ans == count:
            return True



a = Solution.checkOnesSegment(None,'101')
print(a)
