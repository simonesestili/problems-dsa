class Solution:
    def minCost(self, colors, time):
        prev, ans, mx, s = '-', 0, 0, 0
        for t, c in zip(time, colors):
            if c != prev:
                ans += s - mx
                mx = s = 0
            prev = c
            mx = max(mx, t)
            s += t
        return ans + s - mx
