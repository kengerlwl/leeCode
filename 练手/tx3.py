import bisect

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return [newInterval]
        findRight = {}
        findLeft = {}
        for l, r in intervals:
            findRight[l] = r
            findLeft[r] = l

        indexLeft = sorted(findRight)
        indexRight = sorted(findLeft)


        l = newInterval[0]
        r= newInterval[1]

        tmp = bisect.bisect_left(indexLeft, r)
        print(indexLeft, tmp, r)

        if tmp >= len(intervals) or tmp< 0 or r < intervals[tmp][0]  :
            tmp -=1

        tmpright = intervals[tmp][1]
        tmpright = max(r, tmpright)

        tmp = bisect.bisect_right(indexRight, l)
        # if  tmp >= len(intervals) :
        #     tmp -=1
        print(indexRight, tmp)
        tmpleft = l
        try:
            tmpleft = min(newInterval[tmp][1], l)
        except:
            pass


        print(tmpleft, tmpright)

        # print(tmp)

        def judge(l, r):
            if l > tmpright or r < tmpleft:
                return False
            else:
                return True

        ans = []
        flag = True
        for l, r in intervals:
            if not judge(l, r):
                ans.append([l,r])
            else:
                if flag:
                    ans.append([tmpleft, tmpright])
                    flag = False

        if ans.__eq__(intervals):
            ans.append([tmpleft, tmpright])

        print(ans)
        return ans



Solution.insert(None,[[1,5]],
[6,8]


                )

