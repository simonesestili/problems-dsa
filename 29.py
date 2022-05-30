class Solution:
    def divide(self, p, q):
        neg = (p < 0) != (q < 0)
        p, q = map(abs, [p, q])

        quotient, pwr, curr = 0, 0, q
        while curr << 1 <= p:
            pwr, curr = pwr + 1, curr << 1

        while q <= p:
            quotient, p = quotient + (1 << pwr), p - curr
            while curr > p:
                pwr, curr = pwr - 1, curr >> 1

        return max(-quotient, -(1 << 31)) if neg else min(quotient, (1 << 31) - 1)
