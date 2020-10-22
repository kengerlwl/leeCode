class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        j =0
        pre = typed[0]
        for i in range(len(name)):
            c = name[i]
            if c != typed[j]:
                while pre == typed[j]:
                    j+=1
                # print(c, [j])
                if j >= len(typed):
                    return False

                if c != typed[j]:
                    print('false')
                    return False

                pre = typed[j]
            pre = typed[j]
            j+=1
            if j >= len(typed):
                return False
        return True

        print('true')


Solution.isLongPressedName(None,name = "leelee", typed = "lleeelee")


