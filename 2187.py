class Solution:
    def minimumTime(self, time, total):
        valid = lambda t: sum(t // x for x in time) >= total

        lo, hi = 0, min(time) * total
        while lo < hi:
            mid = (lo + hi) >> 1
            if valid(mid): hi = mid
            else: lo = mid + 1

        return lo
