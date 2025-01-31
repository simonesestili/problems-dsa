class Solution:
    def mincostTickets(self, days, costs):

        @cache
        def dp(i):
            if i == len(days): return 0
            week = bisect_right(days, days[i] + 6)
            month = bisect_right(days, days[i] + 29)
            return min(costs[0] + dp(i + 1), costs[1] + dp(week), costs[2] + dp(month))

        return dp(0)
