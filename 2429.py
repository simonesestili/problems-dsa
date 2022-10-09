class Solution:
    def minimizeXor(self, a, b):
        diff = a.bit_count() - b.bit_count()
        for i in range(32):
            if diff > 0 and a >> i & 1:
                a -= 1 << i
                diff -= 1
            elif diff < 0 and not a >> i & 1:
                a |= 1 << i
                diff += 1
        return a
