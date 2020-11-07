#
# 考虑从高位高位向低位依次确定每一个位置的字符。
#
# 如果我们在最高位放置了 \texttt{H}H，那么剩余的 (h-1,v)(h−1,v) 就是一个规模减少的相同问题；同理如果我们在最高位放置了 \texttt{V}V，那么剩余的 (h,v-1)(h,v−1) 也是一个规模减少的相同问题。

#https://leetcode-cn.com/problems/kth-smallest-instructions/solution/di-k-tiao-zui-xiao-zhi-ling-by-zerotrac2/


class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        ans = list()
        for i in range(h + v):
            if h > 0:
                o = math.comb(h + v - 1, h - 1)
                if k > o:
                    ans.append("V")
                    v -= 1
                    k -= o
                else:
                    ans.append("H")
                    h -= 1
            else:
                ans.append("V")
                v -= 1
        return "".join(ans)

Solution.kthSmallestPath(None, destination = [2,3], k = 3)