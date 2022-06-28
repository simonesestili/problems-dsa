MOD = 10 ** 9 + 7
class Solution:
    def countHousePlacements(self, n):
        dp = [1, 2] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] * dp[n] % MOD

