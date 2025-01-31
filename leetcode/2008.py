class Solution:
    def maxTaxiEarnings(self, n, rides):
        starts = defaultdict(list)
        for start, end, tip in rides: starts[start].append((end, tip))

        @cache
        def dp(i):
            if i > n: return 0
            ans = 0
            for end, tip in starts[i]:
                ans = max(ans, end - i + tip + dp(end))
            return max(ans, dp(i+1))

        return dp(1)

