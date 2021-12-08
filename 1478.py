class Solution:
    def minDistance(self, houses, k):
        n = len(houses)
        houses.sort()
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = houses[(i + j) // 2]
                for m in range(i, j + 1):
                    costs[i][j] += abs(houses[m] - mid)

        @lru_cache(None)
        def dp(k, i):
            if not k and i == n: return 0
            if not k or i == n: return float('inf')
            ans = float('inf')
            for j in range(i, n):
                ans = min(ans, costs[i][j] + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)
