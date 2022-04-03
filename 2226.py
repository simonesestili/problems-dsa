class Solution:
    def maximumCandies(self, candies, k):
        valid = lambda amt: sum(x // amt for x in candies) >= k

        lo, hi = 0, max(candies)
        while lo < hi:
            cand = (lo + hi + 1) >> 1
            if valid(cand): lo = cand
            else: hi = cand - 1

        return lo
