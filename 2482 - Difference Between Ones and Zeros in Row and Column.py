class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        ones_i, ones_j = [0]*m, [0]*n

        for i in range(m):
            ones_i[i] = sum(grid[i])

        for j in range(n):
            ones_j[j] = sum([grid[k][j] for k in range(m)])

        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*ones_i[i] - n + 2*ones_j[j] - m

        return grid