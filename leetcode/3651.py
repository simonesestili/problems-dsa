class Solution:
    def minCost(self, grid, k):
        m, n = len(grid), len(grid[0])
        dp, best = [[0] * n for _ in range(m)], defaultdict(lambda: inf)
        for i in range(m):
            for j in range(n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j] if i else inf, dp[i][j-1] if j else inf) if i or j else 0
                best[grid[i][j]] = min(best[grid[i][j]], dp[i][j])

        for _ in range(k):
            tps, curr = {}, inf
            for v, cost in sorted(best.items(), reverse=True):
                curr = min(curr, cost)
                tps[v] = curr

            best = defaultdict(lambda: inf)
            for i in range(m):
                for j in range(n):
                    move = grid[i][j] + min(dp[i][j], dp[i-1][j] if i else inf, dp[i][j-1] if j else inf)
                    dp[i][j] = min(move, tps[grid[i][j]])
                    best[grid[i][j]] = min(best[grid[i][j]], dp[i][j])

        return dp[-1][-1]
