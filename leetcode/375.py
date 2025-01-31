class Solution:
    def getMoneyAmount(self, n):

        @cache
        def dp(i, j):
            if j - i <= 1: return i if j - i else 0
            best = float('inf')
            for k in range(i + 1, j):
                best = min(best, k + max(dp(i, k - 1), dp(k + 1, j)))
            return best

        return dp(1, n)
