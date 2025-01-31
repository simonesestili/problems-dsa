class Solution:
    def minNonZeroProduct(self, p):
        M = pow(10, 9) + 7
        x = pow(2, p) - 1
        return pow(x - 1, x // 2, M) * x % M
