class Solution:
    def nthMagicalNumber(self, n, a, b):
        a, b = sorted([a, b])
        c = self.lcd(a, b)
        lo, hi = a, a * n
        while lo < hi:
            cand = (lo + hi) // 2
            previous = cand // a + cand // b - cand // c
            if previous > n:
                hi = cand - 1
            elif previous < n:
                lo = cand + 1
            else:
                hi = cand
        return lo % (10 ** 9 + 7)

    def lcd(self, a, b):
        return (a * b) // self.gcd(a, b)

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
