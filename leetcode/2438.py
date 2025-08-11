MOD = 10**9+7
class Solution:
    def productQueries(self, n, queries):
        powers = []
        while n:
            powers.append(n & -n)
            n -= n & -n

        k = len(powers)
        dp = [[0] * k for _ in range(k)]
        for i in range(k):
            dp[i][i] = powers[i]
            for j in range(i+1, k):
                dp[i][j] = dp[i][j-1] * powers[j] % MOD

        return [dp[l][r] for l, r in queries]

