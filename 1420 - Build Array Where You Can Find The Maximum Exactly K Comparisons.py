class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        N, M, K = n, m, k
        mod = 1e9+7

        dp = [[[0 for _ in range(K+1)] for _ in range(M+1)] for _ in range(N+1)]

        for i in range(1, N+1):
            for j in range(1, M+1):
                for k in range(1, K+1):
                    if i < k: continue
                    elif i == k == 1:
                        dp[i][j][k] = 1
                    else:
                        cnt = 0
                        for x in range(1, M+1):
                            if x >= j:
                                cnt += dp[i-1][j][k]
                            else:
                                cnt += dp[i-1][x][k-1]
                            cnt %= mod

                        dp[i][j][k] = cnt

        return int(sum(dp[n][y][k] for y in range(1, M+1)) % mod) 