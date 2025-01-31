class Solution:
    def minDistance(self, a, b):
        m, n = len(a), len(b)

        @cache
        def dp(i=0, j=0):
            if i >= m: return n - j
            if j >= n: return m - i
            if a[i] == b[j]: return dp(i + 1, j + 1)
            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))

        return dp()
