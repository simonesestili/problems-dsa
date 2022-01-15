class Solution:
    def minEatingSpeed(self, piles, h):
        n, piles = len(piles), sorted(piles, reverse=True)
        k, common, extra = 0, h // n, h % n
        for i, count in enumerate(piles):
            curr = ceil(count / (common + 1)) if i < extra else ceil(count / common)
            k = max(k, curr)
        return k

