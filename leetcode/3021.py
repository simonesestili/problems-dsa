class Solution:
    def flowerGame(self, n, m):
        xodd, xeven = (n + 1) // 2, n // 2
        yodd, yeven = (m + 1) // 2, m // 2
        return xodd * yeven + xeven * yodd
