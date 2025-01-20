class Solution:
    def minimizeXor(self, a, b):
        extra = a.bit_count() - b.bit_count()
        for i in range(32):
            if extra > 0 and a >> i & 1:
                a -= 1 << i
                extra -= 1
            elif extra < 0 and not a >> i & 1:
                a += 1 << i
                extra += 1
        return a
