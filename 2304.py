class Solution:
    def minPathCost(self, grid, costs):
        m, n = len(grid), len(grid[0])

        @cache
        def dp(row, col):
            if row == m - 1: return grid[row][col]
            return min(dp(row + 1, i) + costs[grid[row][col]][i] + grid[row][col] for i in range(n))

        return min(dp(0, col) for col in range(n))
