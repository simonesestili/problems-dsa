class Solution:
    def minCost(self, colors, cost):
        time = curr = mx = prev = 0
        for c, t in zip(colors, cost):
            if c != prev:
                time += curr - mx
                curr = mx = 0
            mx = max(mx, t)
            curr += t
            prev = c
        return time + curr - mx

