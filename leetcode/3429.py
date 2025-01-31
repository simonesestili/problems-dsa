class Solution:
    def minCost(self, n, cost):

        @cache
        def dp(i, l, r):
            if i == n // 2: return 0

            ans = inf
            for lp in range(3):
                for rp in range(3):
                    if l == lp or r == rp or lp == rp: continue
                    ans = min(ans, cost[i][lp] + cost[n-i-1][rp] + dp(i + 1, lp, rp))

            return ans

        return dp(0, -1, -1)
