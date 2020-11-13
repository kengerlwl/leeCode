class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet ={}
        for i in s:
            if i in charSet:
                charSet[i] +=1
            else:
                charSet[i] =1
        a =sorted(charSet, key= lambda x:charSet[x])
        print(a) # 排序后的索引
        pre = a[0]


        count =0
        exist = {}

        # 找到应该向前减少个数
        def find(c):
            num = charSet[c]
            num -=1
            while num>0:
                if num not in exist:
                    return charSet[c] - num
                num -=1
            return charSet[c]

            return 1
        # exist[pre] = True
        for i in range(1, len(a)):
            exist[charSet[pre]] = True
            now = a[i]
            if charSet[now] == charSet[pre]: # 两个频率一样的词。
                tmp = find(now)
                count +=tmp
                # print(now, tmp)
                charSet[now] -= tmp
                exist[charSet[now]] = True

                continue
            pre = now

        print(count)
        return count









Solution.minDeletions(None,"abcabc")
