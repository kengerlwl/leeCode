from functools import lru_cache


class Solution:
    """@lru_cache 装饰器是 Python 语言提供的可供记忆化搜索的利器
    相当于将该参数的（输入，输出）对缓存起来
    在以相同的输入调用该函数时，就可以避免计算，直接返回输出
    """

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        @lru_cache(None)
        def getTrans(stats, ch):
            """这是计算关于 stats 的转移函数
            输入为 stats 和 d
            输出为转移的结果 g_s(stats, d)"""

            u = ord(ch) - 97
            # 这是 KMP 算法的一部分
            # 把 evil 看作「模式串」，stats 看作「主串」匹配到的位置
            while stats > 0 and evil[stats] != ch:
                stats = fail[stats - 1]
            return stats + 1 if evil[stats] == ch else 0


        # 对子情况进行搜搜
        @lru_cache(None)
        def dfs(pos, stats, bound):
            """这是用来进行记忆化搜索的函数
            输入为 pos, stats 和 bound
            输出为 f[pos][stats][bound]"""

            # 如果匹配到了 evil 的末尾
            # 说明字符串不满足要求了
            # 返回 0
            if stats == len(evil):
                return 0
            # 如果匹配到了上下界的末尾
            # 说明找到了一个满足要求的字符串
            # 返回 1
            if pos == len(s1):
                return 1

            ans = 0
            # 计算第 pos 位可枚举的字符下界
            l = (ord(s1[pos]) if bound & 1 else ord('a'))
            # 计算第 pos 位可枚举的字符上界
            r = (ord(s2[pos]) if bound & 2 else ord('z'))
            for u in range(l, r + 1):
                ch = chr(u)
                nxt_stats = getTrans(stats, ch)
                # 这里写得较为复杂
                # 本质上就是关于 bound 的转移函数
                # 可以根据自己的理解编写
                nxt_bound = (ch == s1[pos] if bound & 1 else 0) ^ ((ch == s2[pos]) << 1 if bound & 2 else 0)
                ans += dfs(pos + 1, nxt_stats, nxt_bound)
            return ans % 1000000007

        m = len(evil)
        # 这是用来帮助计算关于 stats 的转移函数的 fail 数组
        fail = [0] * m
        # 这是 KMP 算法的一部分
        # 把「evil」看作模式串，得到它的 fail[] 数组
        for i in range(1, m):
            j = fail[i - 1]
            while j > 0 and evil[j] != evil[i]:
                j = fail[j - 1]
            if evil[j] == evil[i]:
                fail[i] = j + 1

        # 答案即为 f[0][0][3]
        return dfs(0, 0, 3)
