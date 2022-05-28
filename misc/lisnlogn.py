class Solution:
    def lis(self, arr):
        piles = []
        for x in arr:
            idx = bisect_left(piles, x)
            if idx == len(piles): piles.append(x)
            else: piles[idx] = x

        return len(piles)
