class Solution:
    def minimumIncompatibility(self, nums, k):
        n = len(nums)
        # 特殊判断，如果元素数量等于组数
        if n == k:
            return 0

        value = dict()
        for sub in range(1 << n):
            # 判断 sub 是否有 n/k 个 1
            if bin(sub).count("1") == n // k:
                # 使用哈希表进行计数
                freq = set()
                flag = True
                for j in range(n):
                    if sub & (1 << j):  # 一位一位的统计。 如果这个位为1，那么就会为true
                        # 任意一个数不能出现超过 1 次
                        if nums[j] in freq:
                            flag = False
                            break
                        freq.add(nums[j])

                # 如果满足要求，那么计算 sub 的不兼容性
                if flag:
                    value[sub] = max(freq) - min(freq)

        f = dict()
        f[0] = 0
        for mask in range(1 << n):
            # 判断 mask 是否有 n/k 倍数个 1
            if bin(mask).count("1") % (n // k) == 0:
                # 枚举子集
                sub = mask
                while sub > 0:
                    if sub in value and mask ^ sub in f:  #  是合理的子集。并且删减后可以是另一个小规模的状态。
                        if mask not in f:# 初始化
                            f[mask] = f[mask ^ sub] + value[sub]
                        else: # 更新
                            f[mask] = min(f[mask], f[mask ^ sub] + value[sub])
                    sub = (sub - 1) & mask #枚举子集。

        return -1 if (1 << n) - 1 not in f else f[(1 << n) - 1]


