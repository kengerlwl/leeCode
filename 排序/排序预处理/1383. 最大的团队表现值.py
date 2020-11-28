class Solution:
    class Staff:
        def __init__(self, s, e):
            self.s = s
            self.e = e

        def __lt__(self, that):
            return self.s < that.s

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        v = list()
        for i in range(n):
            v.append(Solution.Staff(speed[i], efficiency[i]))
        v.sort(key=lambda x: -x.e)

        q = list()
        ans, total = 0, 0
        for i in range(n):
            minE, totalS = v[i].e, total + v[i].s
            ans = max(ans, minE * totalS)
            heapq.heappush(q, v[i])
            total += v[i].s
            if len(q) == k:
                item = heapq.heappop(q)
                total -= item.s
        return ans % (10 ** 9 + 7)


