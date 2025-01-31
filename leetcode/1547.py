class Solution:
    def minCost(self, n, cuts):
        cuts = sorted(cuts + [0, n])

        @cache
        def dp(left, right):
            i, j = bisect_right(cuts, left), bisect_left(cuts, right)
            if j <= i: return 0
            return min(right - left + dp(left, cuts[k]) + dp(cuts[k], right) for k in range(i, j))

        return dp(0, n)
