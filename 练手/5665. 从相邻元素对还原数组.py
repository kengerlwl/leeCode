class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        f = {}
        start = None
        for a, b in adjacentPairs:
            if a not in f:
                f[a] ={}
                f[a][b] = True
            else:
                f[a][b] = True

            if b not in f:
                f[b] = {}
            f[b][a] = True

        for i in f:
            if len(f[i]) ==1:
                start = i
                break
        print(start)
        # print(f)
        now = start
        last = now
        ans = [start]

        nextNum = list(f[now])[0]
        print(nextNum)
        # return 0
        # print(len(f[]))
        note = {}
        note[start] = True
        while len(f[nextNum]) == 2:
            ans.append(nextNum)
            note[nextNum] = True
            for a in f[nextNum]:
                if a not in note:
                    nextNum = a

            # print(nextNum)
            # print(ans)
        ans.append(nextNum)
        print(ans)
        return ans



Solution.restoreArray(None,[[4,-2],[1,4],[-3,1]])


