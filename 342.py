class Solution:
    def isPowerOfFour(self, n):
        return n > 0 and not n & (n - 1) and not n & 0b0101010101010101010101010101010
