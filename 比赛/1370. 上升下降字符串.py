class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        charSet ={}
        for i in s:
            if i in charSet:
                charSet[i] +=1
            else:
                charSet[i] =1
        # print(charSet)
        # 是否已经选完
        def chech(Set):
            for i in Set:
                if Set[i] != 0:
                    return False
            return True

        index = sorted(charSet)
        # print(index)
        import  copy
        index_re = copy.deepcopy(index)
        index_re.reverse()
        # print(index_re)
        result = ""
        while not chech(charSet):
            for i in index:
                if charSet[i] > 0:
                    result += i
                    charSet[i] -=1

            for i in index_re:
                if charSet[i] > 0:
                    result += i
                    charSet[i] -= 1

        # print(result)
        return result


Solution.sortString(None, "aaaabbbbcccc")