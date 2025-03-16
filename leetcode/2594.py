class Solution:
    def repairCars(self, ranks, n):
        valid = lambda time: sum(int(sqrt(time / r)) for r in ranks) >= n

        lo, hi = 1, min(ranks) * n * n
        while lo < hi:
            cand = (lo + hi) // 2
            if valid(cand): hi = cand
            else: lo = cand + 1
        return lo
