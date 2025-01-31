class Solution:
    def maxCoins(self, piles):
        n, piles = len(piles), sorted(piles)
        return sum(piles[i] for i in range(n - 2, n // 3 - 1, -2))
