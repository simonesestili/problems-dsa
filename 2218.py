class Solution:
    def maxValueOfCoins(self, piles, k):
        n = len(piles)

        @cache
        def dp(i, rem):
            if i >= n or rem == 0: return 0
            ans, curr = dp(i+1, rem), 0
            for j in range(min(rem, len(piles[i]))):
                curr += piles[i][j]
                ans = max(ans, curr + dp(i + 1, rem - j - 1))
            return ans

        return dp(0, k)
