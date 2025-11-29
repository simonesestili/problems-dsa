MOD = 10**9+7
class Solution:
    def numberOfPaths(self, grid, k):
        m, n = len(grid), len(grid[0])
        dp = [[0] * k for _ in range(n)]

        for i in range(m):
            ndp = [[0] * k for _ in range(n)]
            for j in range(n):
                v = grid[i][j] % k

                if i == 0 and j == 0:
                    ndp[0][v] = 1
                    continue
                if i > 0:
                    for r, c in enumerate(dp[j]):
                        if c:
                            ndp[j][(r + v) % k] = (ndp[j][(r + v) % k] + c) % MOD
                if j > 0:
                    for r, c in enumerate(ndp[j - 1]):
                        if c:
                            ndp[j][(r + v) % k] = (ndp[j][(r + v) % k] + c) % MOD

            dp = ndp

        return dp[n - 1][0]
