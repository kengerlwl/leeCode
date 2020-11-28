
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == '':
            if needle =='':
                return 0
            else:
                return -1
        elif needle =='':
            return 0



        # 计算next数组， next[i]代表前i个字符串的最长子串
        def getnext(s):
            n = len(s)
            next = [0,0]  # 第一个0代表空字符串
            for i in range(2, n+1):
                # print(next, s, i-1)
                if s[next[i-1]] == s[i-1]:
                    next.append(next[i-1] +1)
                else:
                    j = next[next[i-1]]
                    while j > 0:
                        if s[j] == s[i-1]:
                            next.append(j+1)
                            break
                        j = next[j]
                    if j ==0:
                        if s[i-1] == s[0]:
                            next.append(1)
                        else:
                            next.append(0)

            return next

        next  =getnext(needle)
        print(next)


        # 构造有限状态机
        def kmp(s, next):  # 一个状态机
            n = len(s)
            state = {'other':True}
            for i in s:
                state[i] = True

            matrix = [{} for i in range(n+1)]

            #初始化
            for i in state:
                matrix[0][i] = 0
            matrix[0][s[0]] =1


            # 归纳法进行递推
            for i in range(1, n+1):

                j = i
                while j> 0:
                    if j >= n:
                        j = next[j]
                        continue
                    char = s[j]
                    if char not in matrix[i]:
                        matrix[i][char] = j+1
                    j = next[j]
                if j ==0:
                    if s[0] not in matrix[i]:
                        matrix[i][s[0]] =1
                for k in state:
                    if k not in matrix[i]:
                        matrix[i][k] = 0
            return matrix, state






        m,state = kmp(needle, next)
        for i in range(len(m)):
            print(i, m[i])
        print(m)


        def search(txt):
            N = len(txt)
            l = len(needle)
            stateNow = 0
            for i in range(N):
                char = txt[i]
                if char in state:
                    stateNow = m[stateNow][char]
                else:
                    stateNow = m[stateNow]['other']

                if stateNow == l:
                    return i- l+1
            return -1

        print(search(haystack))
        return search(haystack)




Solution.strStr(None,"ababcaababcaabc",
"ababcaabc")


