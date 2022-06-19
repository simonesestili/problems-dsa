class Solution:
    def sellingWood(self, m, n, prices):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, price in prices: dp[h][w] = price
        
        for height in range(m + 1):
            for width in range(n + 1):
                for cut in range(1, height // 2 + 1):
                    dp[height][width] = max(dp[height][width], dp[cut][width] + dp[height - cut][width])
                for cut in range(1, width // 2 + 1):
                    dp[height][width] = max(dp[height][width], dp[height][cut] + dp[height][width - cut])

        return dp[m][n]
