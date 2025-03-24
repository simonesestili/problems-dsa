class Solution:
    def countDays(self, days, meetings):
        ans = prev = 0
        for s, e in sorted(meetings):
            if s > prev:
                ans += s - prev - 1
            prev = max(prev, e)
        ans += days - prev
        return ans
