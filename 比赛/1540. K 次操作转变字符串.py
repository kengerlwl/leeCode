# 本质上还是一个应用题
class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        length = len(s)

        if len(s) !=  len(t):
            return False

        val ={}
        for i in range(length):
            dif =  ord(t[i]) - ord(s[i])
            if dif == 0:
                continue
            if dif <0:
                dif += 26
            if dif > k:
                return False
            else:
                if dif not in val:
                    val[dif] = dif
                else:
                    cur = val[dif]
                    cur +=  26
                    if cur > k:
                        return False
                    else:
                        val[dif] = cur

        return True


Solution.canConvertString(None, s = "input", t = "ouput", k = 9)
