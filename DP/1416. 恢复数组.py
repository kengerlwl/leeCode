
#利用好分类思想
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(s)
        # 递推的边界条件，f[0] = 1
        f = [1] + [0] * n
        for i in range(1, n + 1):
            num, base = 0, 1
            j = i - 1
            # 倒序枚举 j，最多只需要枚举 10 个
            while j >= 0 and i - j <= 10:
                # 在高位添加当前的数字，得到第 j+1 到 i 个数字组成的数
                # 注意 s 的下标是从 0 开始的
                num += (ord(s[j]) - 48) * base
                if num > k:
                    break
                # 判断是否有前导 0
                if s[j] != "0":
                    f[i] += f[j]
                base *= 10
                j -= 1
            f[i] %= mod
        return f[n]

