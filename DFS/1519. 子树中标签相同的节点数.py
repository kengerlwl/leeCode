# class Solution:
#     def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
#         ans = [0 for i in range(n)]
#         dtree = defaultdict(list)
#         for e in edges:
#             dtree[e[0]].append(e[1])
#             dtree[e[1]].append(e[0])
#
#         def dfs(i, parent):
#             cnt = Counter()
#             for ni in dtree[i]:
#                 if ni != parent:
#                     cnt += dfs(ni, i)
#             cnt[labels[i]] += 1
#             ans[i] = cnt[labels[i]]
#             return cnt
#
#         dfs(0, None)
#
#         return ans
#
#
# 作者：oymshw
# 链接：https: // leetcode - cn.com / problems / number - of - nodes - in -the - sub - tree -
# with-the - same - label / solution / 5465zi-shu-zhong-biao-qian-xiang-tong-de-jie-dian- /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



#我的没打表，会超时
class Solution(object):

    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        tmp = []
        num = set()

        # 树得根节点为0
        num.add(edges[0][0])
        num.add(edges[0][1])
        a, b = edges[0]
        if a > b:
            edges[0] = [b, a]

        for a, b in edges:
            if a in num:
                tmp.append([a, b])
                num.add(b)
            else:

                tmp.append([b, a])
        edges = tmp

        print(edges)

        def dfs(i, t):
            queue = []
            queue.append(i)
            count = 0
            while queue:
                top = queue.pop()
                if t == labels[top]:
                    count += 1
                for j in edges:
                    if j[0] == top:  # 加入队列
                        queue.append(j[1])

            return count

        res = []
        for i in range(n):
            target = labels[i]
            print(i, target)
            ans = dfs(i, target)
            res.append(ans)

        print(res)
        return res


Solution.countSubTrees(None,

7
,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
,"abaedcd"
)
