# 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
#
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
#
# 示例 1:
#
# 输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出: [20,24]
# 解释:
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 注意:
#
# 给定的列表可能包含重复元素，所以在这里升序表示 >= 。
# 1 <= k <= 3500
# -105 <= 元素的值 <= 105
# 对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。



#这个解法很强了， 深刻运用了数据结构。
class Solution:
    def smallestRange(self, nums):
        from queue import PriorityQueue  # 最小堆，里面元素自动排列，     ！！！！！！！！！！！！！！！！
        q = PriorityQueue()
        N = len(nums)
        INF = 10 ** 9
        maxv = -INF
        start, end = -INF, INF

        #先把所有序列得头节点放进去， 也就是最小得放进去    i代表在哪个数组，  j代表第几个
        for i in range(N):
            q.put((nums[i][0], i, 0))
            maxv = max(maxv, nums[i][0])

        # 然后利用数据结构队列，进行遍历
        while q.qsize() == N:

            #一个一个遍历
            v, i, j= q.get()
            print(v, i,j)



            # 是否需要更新
            if maxv - v < end - start:
                start, end = v, maxv


            # 是否可以将数据进栈
            if j + 1 < len(nums[i]):
                nv = nums[i][j + 1]
                q.put((nv, i, j + 1))
                maxv = max(maxv, nv)

        return [start, end]

ans  = Solution.smallestRange(None, [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
print(ans)