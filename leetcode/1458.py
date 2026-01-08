class Solution:
    def maxDotProduct(self, a, b):
        n, m = len(a), len(b)

        @cache
        def dp(i, j, choose):
            if i >= n or j >= m:
                return 0 if choose else -inf
            return max(a[i] * b[j] + dp(i + 1, j + 1, True), dp(i + 1, j, choose), dp(i, j + 1, choose))

        return dp(0, 0, False)
