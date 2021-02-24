class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        def judge(s):
            l = 0
            r = len(s)-1

            if r == l:
                return 1
            #
            # if s.count(s[0]) == len(s):
            #     return 0

            if s[l] != s[r]:
                return len(s)
            else:
                ans = 0
                c = s[l]
                while l <= r:
                    f = False
                    if s[l] == c:
                        l+=1
                        ans+=1
                        f = True
                    # print(l,r)
                    if l > r:
                        break
                    if s[r] == c:
                        r -=1
                        ans+=1
                        f = True

                    if not f:
                        if s[l] != s[r] or r - l + 1<2:
                            break
                        else:
                            c = s[l]
                # print(s[l:r+1])
                if l > r:
                    return 0

                return judge(s[l:r+1])

        ans  = judge(s)
        print(ans)
        return ans

Solution.minimumLength(None,"acaca")