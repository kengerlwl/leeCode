class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        m = len(languages)
        f = {}
        for i in range(1, m+1):
            f[i] = {}
            lan = languages[i-1]
            for j in lan:
                f[i][j] = True  #第i个用户，会第几个语言

        # print(f)

        wrong = []
        for i in friendships:
            a = i[0]
            b = i[1]
            flag  = False
            for lan in f[a]:
                if lan in f[b]:
                    flag = True #有一门共同语言
            if not flag:
                wrong.append(i)

        # print(wrong)
        ans ={}
        for a,b in wrong:
            if a not in ans:
                ans[a] = True
            if b not  in ans:
                ans[b] = True
        count = {}
        maxV  = 0
        for i in ans:
            for j in f[i]:
                if j in count:
                    count[j]+=1
                else:
                    count[j] = 1
                maxV = max(maxV, count[j])

        return len(ans) - maxV


a= Solution.minimumTeachings(None,n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]])
print(a)
