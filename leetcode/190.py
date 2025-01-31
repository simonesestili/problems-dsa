class Solution:
    def reverseBits(self, n):
        for i in range(16):
            left, right = n >> (31 - i) & 1, n >> i & 1
            n &= (1 << 32) - (1 << 31 - i) - (1 << i) - 1
            n |= (left << i) + (right << 31 - i)

        return n
