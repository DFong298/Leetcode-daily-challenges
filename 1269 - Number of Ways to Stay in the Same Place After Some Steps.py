class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = int(1e9) + 7
        n = min(arrLen, steps)

        dp = [[0] * n for _ in range(steps+1)]
        dp[0][0] = 1
        
        for i in range(1, steps+1):
            for j in range(n):
                left = 0 if j == 0 else dp[i-1][j-1]
                right = 0 if j == n-1 else dp[i-1][j+1]
                dp[i][j] = (dp[i-1][j] + left + right) % mod

        return dp[-1][0]