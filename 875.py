class Solution:
    def minEatingSpeed(self, piles, h):
        valid = lambda k: sum([ceil(x / k) for x in piles]) <= h
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            if valid(k): hi = k
            else: lo = k + 1
        return lo
