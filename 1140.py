class Solution:
    def stoneGameII(self, piles):
        n, total = len(piles), sum(piles)

        @cache
        def dp(i, m):
            if i >= n: return 0
            best, curr = float('-inf'), 0
            for j in range(i, min(i + 2 * m, n)):
                curr += piles[j]
                best = max(best, curr - dp(j + 1, max(j - i + 1, m)))
            return best

        return total - ((total - dp(0, 1)) // 2)
