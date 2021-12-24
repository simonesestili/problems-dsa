class Solution:
    def isPowerOfFour(self, n):
        return n > 0 and not n & (n - 1) and not (n - 1) % 3
