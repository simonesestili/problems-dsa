class Solution:
    def nthUglyNumber(self, n, a, b, c):
        a, b, c = sorted([a, b, c])

        def index(x):
            return (x // a + x // b + x // c - 
                    x // self.lcm(a, b) - x // self.lcm(b, c) - x // self.lcm(a, c) +
                    x // self.lcm(a, self.lcm(b, c)))

        lo, hi = a, a * n
        while lo < hi:
            mid = (lo + hi) // 2
            idx = index(mid)
            if idx < n: lo = mid + 1
            else: hi = mid
        return lo

    def gcd(self, a, b):
        if a == 0: return b
        return gcd(b % a, a)

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)
