MOD = 10**9+7
class Solution:
    def peopleAwareOfSecret(self, n, delay, forget):
        dp = [0, 1] + [0] * (n - 1)
        for day in range(2, n + 1):
            for i in range(day - forget + 1, day - delay + 1):
                dp[day] = (dp[day] + dp[i]) % MOD

        ans = 0
        for i in range(n - forget + 1, n + 1):
            ans = (ans + dp[i]) % MOD
        return ans
