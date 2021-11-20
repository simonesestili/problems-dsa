class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if grid[0][0] else 1
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    left = 0 if not j else dp[i][j - 1]
                    right = 0 if not i else dp[i - 1][j]
                    dp[i][j] += left + right
        return dp[-1][-1]
