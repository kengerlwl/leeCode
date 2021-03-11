class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """


        def judge(s):
            l = len(s)
            for i in range(l):
                if s[i] != s[l - i - 1]:
                    return False
            return True

        import copy
        def get(s):
            if len(s) == 1:
                return [s]
            if len(s) == 0:
                return []
            l = len(s)
            ans = []
            for i in range(1, l + 1):
                left = s[0:i]  # 当前是回文
                print(left)

                if judge(left):
                    left = [str(left)]
                    rights = get(s[i:l])
                    for j in rights:
                        print(left, j)
                        ans.append(copy.deepcopy(left) + j)
            print(ans)
            return ans

        print(get(s))


Solution.partition(None, 'aab')