
# DP解法
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m, n = len(s), len(p)
#
#         def matches(i: int, j: int) -> bool:
#             if i == 0:
#                 return False
#             if p[j - 1] == '.':
#                 return True
#             return s[i - 1] == p[j - 1]
#
#         f = [[False] * (n + 1) for _ in range(m + 1)]
#         f[0][0] = True
#         for i in range(m + 1):
#             for j in range(1, n + 1):
#                 if p[j - 1] == '*':
#                     f[i][j] |= f[i][j - 2]
#                     if matches(i, j - 1):
#                         f[i][j] |= f[i - 1][j]
#                 else:
#                     if matches(i, j):
#                         f[i][j] |= f[i - 1][j - 1]
#         return f[m][n]


# 状态机解法

class node:
    def __init__(self):
        self.index = 0
        self.next= {

        }

        # next[a] = newNode 经过条件a到达下一个节点 ’$'代表不需要条件


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def creatStateMa(p):
            next = p[0]
            startNode = node()
            index =0
            curNode = startNode
            i =0
            while i <len(p):
                now = p[i]
                if i+1 == len(p):
                    next = now
                else:
                    next = p[i+1]


                print(now, next)


                if next =="*":
                    curNode.index = index
                    index +=1
                    curNode.next['$'] = node()
                    curNode = curNode.next['$']
                    curNode.index = index
                    index +=1

                    curNode.next[now] = curNode
                    i+=2
                else:
                    if now not in curNode.next:
                        curNode.next[now] = node()
                        curNode = curNode.next[now]
                        i+=1
                    else:
                        indexc = sorted(curNode.next)

                        if len(curNode.next) == 1 and curNode == curNode.next[indexc[0]]:
                            curNode.next[now] = node()
                            curNode = curNode.next[now]
                        i+=1


            # print(startNode.next['$'].next['c'].next['$'].next['b'].next)


            return startNode

        start = creatStateMa(p)
        now = start
        # print(s[1:len(s)])


        def match(s, start):


            flag = False

            #空字符 要能确保后一级
            if '$' in start.next:
                tmp = match(s, start.next['$'])
                flag = flag or tmp

                print('$', tmp,s)

            if flag:
                return flag

            if len(s) ==0 :
                if start.next =={}:
                    return True
                index = sorted(start.next)

                if len(start.next)==1 and start == start.next[index[0]]:
                    return True

                return False
            startChar = s[0]



            #匹配上了
            if startChar in start.next:
                tmp = match(s[1:len(s)], start.next[startChar])
                flag = flag or tmp
                print(startChar,tmp, s)

            #通配符
            if '.' in start.next:
                tmp = match(s[1:len(s)], start.next['.'])
                flag = flag or tmp

                print('.',tmp,s)

            #空字符
            if '$' in start.next:
                tmp = match(s, start.next['$'])
                flag = flag or tmp

                print('$', tmp,s)

            return flag

        a = match(s, start)
        print(a)
        return a



Solution.isMatch(None,"a",
".*..a*")
