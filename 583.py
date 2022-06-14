class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        @cache
        def dp(i, j):
            if i == m or j == n: return 0
            if word1[i] == word2[j]: return 1 + dp(i + 1, j + 1)
            return max(dp(i + 1, j), dp(i, j + 1))

        return m + n - 2 * dp(0, 0)
