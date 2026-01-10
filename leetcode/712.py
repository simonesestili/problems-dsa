class Solution:
    def minimumDeleteSum(self, a, b):
        m, n = len(a), len(b)

        @cache
        def dp(i, j):
            if i >= m:
                return sum(ord(c) for c in b[j:])
            if j >= n:
                return sum(ord(c) for c in a[i:])
            if a[i] == b[j]:
                return dp(i + 1, j + 1)
            return min(ord(a[i]) + dp(i + 1, j), ord(b[j]) + dp(i, j + 1))

        return dp(0, 0)
