class Solution:
    def integerBreak(self, n):
        if n <= 3: return n - 1
        if n % 3 == 1: return pow(3, n // 3 - 1) * 4
        if n % 3 == 2: return pow(3, n // 3) * 2
        return pow(3, n // 3)
