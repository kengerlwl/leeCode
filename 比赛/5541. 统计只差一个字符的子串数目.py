class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        ans = 0
        for i in range(m):
            for j in range(n):
                diff = 0
                k = 0
                while i + k < m and j + k < n:
                    diff += int(s[i + k] != t[j + k])
                    if diff > 1:
                        break
                    if diff == 1:
                        ans += 1
                    k += 1
        return ans