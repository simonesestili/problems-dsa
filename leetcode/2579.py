class Solution:
    def coloredCells(self, n):
        corner = n * (n - 1) // 2
        w = 2 * n - 1
        return w * w - 4 * corner
