class Solution:
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        dp = [1] * m

        for i in range(1, m):
            for j in range(i):
                if all(strs[k][i] >= strs[k][j] for k in range(n)):
                    dp[i] = max(dp[i], dp[j] + 1)

        return m - max(dp)
