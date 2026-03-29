class Solution:
    def minNumberOfSeconds(self, h, times):
        lo, hi = 1, h * (h + 1) * min(times) // 2
        while lo < hi:
            s = (lo + hi) // 2
            if sum(int((isqrt(t*t+8*s*t) - t) / (2 * t)) for t in times) >= h:
                hi = s
            else:
                lo = s + 1
        return lo
