class Solution:
    def myPow(self, x, n):
        if not n: return 1
        extra, neg, n = 1, n < 0, abs(n)

        while n > 1:
            if n & 1: extra *= x
            n >>= 1
            x *= x

        return 1 / (x * extra) if neg else x * extra
