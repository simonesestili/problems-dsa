class Solution:
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        shifted = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r, c = divmod((i * n + j + k) % (m * n), n)
                shifted[r][c] = grid[i][j]

        return shifted
