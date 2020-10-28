class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target ={}
        now={}
        for i in p:
            if i in target:
                target[i]+=1
            else:
                now[i] =0
                target[i] =1
        now['other'] =0
        print(target)

        def judge(tmp):
            for i in target:
                if target[i] != tmp[i]:
                    return False
            return True

        if len(s) ==0:
            return []

        l =0
        r=0
        if s[l] in target:
            now[s[l]] += 1
        else:
            now['other'] += 1

        ans =[]

        while r < len(s):
            if r - l < len(p)-1:
                r+=1
                if r == len(s):
                    break

                if s[r] in target:
                    now[s[r]] +=1
                else:
                    now['other']+=1
                continue
            # print(l,r)
            # print(now)
            if judge(now):
                # print(now)
                # print(l,r)
                ans.append(l)

                # print(l)
            l+=1
            if s[l-1] in target:
                now[s[l-1]] -=1
            else:
                now['other'] -= 1
        print(ans)
        return ans



Solution.findAnagrams(None,"cbaebabacd",
"abc")