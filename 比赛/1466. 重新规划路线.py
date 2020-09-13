class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        final = []

        queue = [0]

        flag = [True for n in range(n-1)]
        print(flag)
        count = 0

        while len(queue) !=0:
            top = queue.pop()

            for ix, i in enumerate(connections):
                a = i[0]
                b = i[1]
                if flag[ix]:

                    if a == top:
                        queue.append(b)
                        final.append([a, b])
                        flag[ix] = False
                        count+=1

                    if b == top:
                        queue.append(a)
                        final.append([b, a])
                        flag[ix] = False
        print(count)
        return count



# python3   利用空间换时间。减少遍历
#
# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         edge = [[] for _ in range(n)]
#         for p, c in connections:
#             edge[p].append((c, 1))
#             edge[c].append((p, 0))
#         quee = [0]
#         vist = [False] * n
#         vist[0] = True
#         ans = 0
#         while quee:
#             i = quee.pop(0)
#             for n, c in edge[i]:
#                 if not vist[n]:
#                     vist[n] = True
#                     ans += c
#                     quee.append(n)
#         return ans





Solution.minReorder(None,
6,
[[0,1],[1,3],[2,3],[4,0],[4,5]])