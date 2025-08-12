MOD = 10**9+7
class Solution:
    def numberOfWays(self, n, x):
        dp, b = [1] + [0] * n, 1
        while b ** x <= n:
            p = b ** x
            for rem in range(n, p - 1, -1):
                dp[rem] = (dp[rem] + dp[rem - p]) % MOD
            b += 1
        return dp[n]
