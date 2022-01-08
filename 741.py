class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        DIRS = ((1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 1, 0, 1))

        @cache
        def dp(i, j, ii, jj):
            if not (0 <= i < n and 0 <= ii < n and 0 <= j < n and 0 <= jj < n and grid[i][j] != -1 and grid[ii][jj] != -1):
                return float('-inf')
            curr = grid[i][j] if i == ii and j == jj else grid[i][j] + grid[ii][jj]
            if i == n - 1 and j == n - 1: return curr
            return curr + max(dp(i + a, j + b, ii + c, jj + d) for a, b, c, d in DIRS)

        ans = dp(0, 0, 0, 0)
        return 0 if ans == float('-inf') else ans
