class Solution:
    def maxRunTime(self, n, power):

        def valid(t):
            p = 0
            for x in power:
                if x >= t: p += t
                else: p += x
            return n * t <= p

        lo, hi = 1, sum(power) // n
        while lo < hi:
            time = (lo + hi + 1) // 2
            if valid(time): lo = time
            else: hi = time - 1

        return lo
