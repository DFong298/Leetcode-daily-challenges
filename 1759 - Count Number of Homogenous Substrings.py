class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 +7
        n = 1
        ans = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                n += 1
            else:
                ans += (n * (n + 1) // 2) % mod
                n = 1
        ans += (n * (n + 1) // 2) % mod
        return ans % mod