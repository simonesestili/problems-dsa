class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[0 if not j else float('inf') for j in range(amount + 1)] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                diff = j - coins[i]
                left = float('inf') if diff < 0 else 1 + dp[i][diff]
                dp[i][j] = min(left, float('inf') if i == n - 1 else dp[i + 1][j])
        ans = dp[0][-1]
        return -1 if ans == float('inf') else ans
