class Solution:
    def uniquePathsWithObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)] 

        dp[0][0] = grid[0][0] ^ 1
        for row in range(m):
            for col in range(n):
                if grid[row][col]: continue
                print(row, col)
                dp[row][col] += 0 if not row else dp[row - 1][col]
                dp[row][col] += 0 if not col else dp[row][col - 1]

        return dp[-1][-1]
