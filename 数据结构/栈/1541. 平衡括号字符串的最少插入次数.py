# 分两种情况
# 1 字符为‘（’
# 直接入栈
# 2 字符为‘）’
# 1）当前为最后一个字符
# 1⃣️栈为空，那么需要拼接一个‘（’和一个‘）’，所以ans += 2
# 2⃣️栈不为空，那么需要拼接一个‘）’，所以ans += 1，同时出栈
# 2）当前不为最后一个字符
# 1⃣️后面一个字符为‘）’
# (1) 栈为空，那么需要拼接一个‘（‘，所以ans += 1
# (2) 栈不为空，那么不需要拼接字符，只需出栈即可，注意i++
# 2⃣️后面一个字符不为‘）’
# (1) 栈为空，那么需要拼接一个‘（‘和一个‘）’，所以ans += 2
# (2) 栈不为空，那么需要拼接一个‘）’，只需出栈即可，由于下一个是‘（’，所以直接i++即可
# 最后就是加上栈中‘（’数量 * 2即可
#


from collections import deque

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = deque()
        i =0
        ans =0
        while i < len(s):
            cur = s[i]
            if cur == '(':
                stack.append(cur)
            elif cur == ')':
                if i == len(s) -1:
                    if len(stack) == 0:
                        ans +=2
                    else:
                        ans +=1
                        stack.pop()
                else:
                    nextC = s[i+1]
                    if nextC == ')':
                        if len(stack) ==0:
                            ans+=1
                        else:
                            stack.pop()
                        i += 1

                    else:
                        if len(stack) ==0:
                            ans +=2
                        else:
                            ans +=1
                            i += 1

            i +=1
        ans += len(stack) * 2
        return ans



