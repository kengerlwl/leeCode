class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        timeend={}
        for i in range(k):
            timeend[i] =0
        import heapq
        valid =[]
        timeline = []
        from sortedcontainers import SortedList

        valid = SortedList(range(k))
        print(valid)



        ans = [0 for i in range(k)]
        for i in range(len(arrival)):

            while len(timeline) > 0:
                t, pos = heapq.heappop(timeline)
                if t <= arrival[i]:
                    valid.add(pos)
                else:
                    heapq.heappush(timeline, (t, pos))
                    break
            if len(valid) == 0:
                continue



            key = valid.bisect_left(i % k)
            if key < len(valid):
                pos = valid[key]
            else:
                pos = valid[0]
            # print(i, pos)
            ans[pos] += 1;
            valid.remove(pos);
            heapq.heappush(timeline, (arrival[i] + load[i], pos))


        # print(ans)
        m = max(ans)
        result =[]
        for index in range(len(ans)):
            if ans[index] == m:
                 result.append(index)
        print(result)
        return result


Solution.busiestServers(None,3,
[1,2,3,4,5],
[5,2,3,3,3] )




