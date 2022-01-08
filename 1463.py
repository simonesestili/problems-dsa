class Solution:
    def cherryPickup(self, grid):
        DIRS = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2))
        m, n = len(grid), len(grid[0])

        @cache
        def dp(row, i, j):
            if row == m or not 0 <= i < n or not 0 <= j < n: return 0
            curr = grid[row][i] if i == j else grid[row][i] + grid[row][j]
            return curr + max(dp(row + 1, i + k, j + l) for k, l in DIRS)

        return dp(0, 0, n - 1)
