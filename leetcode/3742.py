class Solution:
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])

        dp = [[[-1] * (k+1) for _ in range(n)] for _ in range(m)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                costs = bool(grid[r][c])
                for cost in range(k+1):
                    if cost > k - costs:
                        continue
                    if (r, c) == (m-1, n-1):
                        dp[r][c][cost] = grid[r][c]
                        continue
                    ans = max(dp[r+1][c][cost+costs] if r+1 < m else -1, dp[r][c+1][cost+costs] if c+1 < n else -1)
                    if ans != -1:
                        dp[r][c][cost] = grid[r][c] + ans

        return dp[0][0][0]
