class Solution:
    def arrangeCoins(self, n):
        return int((sqrt(1 + 8 * n) - 1) / 2)
