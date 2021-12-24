class Solution:
    def stoneGame(self, piles):
        n = len(piles)

        @cache
        def dp(i, j):
            if i > j: return 0
            if (i + j - n) % 2:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))

        return dp(0, n - 1) > 0
