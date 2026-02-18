class Solution:
    def hasAlternatingBits(self, n: int):
        while n:
            if n & 1 ^ (n >> 1 & 1) ^ 1:
                return False
            n >>= 1
        return True

