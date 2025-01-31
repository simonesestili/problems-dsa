class Solution:
    def minCost(self, houses, cost, m, n, target):
        
        @cache
        def dp(i, prev, rem):
            if rem < 0 or (i == m and rem): return float('inf')
            if i == m: return 0
            if houses[i]:
                return dp(i + 1, houses[i], rem - (prev != houses[i]))
            return min(p + dp(i + 1, c + 1, rem - (prev != c + 1)) for c, p in enumerate(cost[i]))

        ans = dp(0, 0, target)
        return ans if ans != float('inf') else -1
