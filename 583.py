class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word2), len(word1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return (m + n) - 2 * dp[0][0]
