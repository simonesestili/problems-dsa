class Solution:
    def minPathCost(self, grid, costs):
        m, n = len(grid), len(grid[0])

        @cache
        def dp(row, col):
            val = grid[row][col]
            if row == m - 1: return val
            return val + min(dp(row + 1, c) + costs[val][c] for c in range(n))

        return min(dp(0, c) for c in range(n))
