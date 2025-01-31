class Solution:
    def minimumTime(self, time, total):
        valid = lambda t: sum(t // tm for tm in time) >= total
        lo, hi = 1, min(time) * total
        while lo < hi:
            cand = (lo + hi) // 2
            if valid(cand): hi = cand
            else: lo = cand + 1
        return lo

