class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1

        for m in range(1, n + 1):
            for root in range(1, m + 1):
                dp[m] += dp[root - 1] * dp[m - root]

        return dp[n]
