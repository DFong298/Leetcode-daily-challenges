class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        a, e, i, o, u = [0]*n, [0]*n, [0]*n, [0]*n, [0]*n
        a[0], e[0], i[0], o[0], u[0] = 1, 1, 1, 1, 1

        for k in range(1, n):
            a[k] = (e[k-1] + i[k-1] + u[k-1]) % mod
            e[k] = (a[k-1] + i[k-1]) % mod
            i[k] = (e[k-1] + o[k-1]) % mod
            o[k] = (i[k-1]) % mod
            u[k] = (i[k-1] + o[k-1]) % mod

        return (a[-1] + e[-1] + i[-1] + o[-1] + u[-1]) % mod