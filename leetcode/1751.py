class Solution:
    def maxValue(self, events, k):
        events.sort()

        @cache
        def dp(i, rem):
            if i >= len(events) or rem == 0: return 0
            nxt = bisect_right(events, events[i][1], lo=i+1, key=lambda e: e[0])
            return max(dp(i+1, rem), events[i][2] + dp(nxt, rem - 1))

        return dp(0, k)
