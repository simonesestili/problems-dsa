class Solution:
    def minScoreTriangulation(self, values):
        @cache
        def dp(i, j):
            if j - i < 2:
                return 0
            return min(values[i] * values[j] * values[k] + dp(i, k) + dp(k, j) for k in range(i + 1, j))
        return dp(0, len(values) - 1)
