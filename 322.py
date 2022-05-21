class Solution:
    def coinChange(self, coins, amount):
        MX = float('inf')
        dp = [0] + [MX] * amount

        for rem in range(1, amount + 1):
            dp[rem] = 1 + min((dp[rem - coin] for coin in coins if rem - coin >= 0), default=MX)

        ans = dp[amount]
        return ans if ans != MX else -1
