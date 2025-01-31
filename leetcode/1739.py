class Solution:
    def minimumBoxes(self, n):
        # most(x) = max blocks used when x of the blocks touch the floor
        def most(x):
            last_row = int(sqrt(0.25 + 2*x) - 0.5)
            extra = x - self.gauss(last_row)
            return self.sum_gauss(last_row) + self.gauss(extra)

        lo, hi = 1, n
        while lo < hi:
            cand = (lo + hi) // 2
            if most(cand) >= n:
                hi = cand
            else:
                lo = cand + 1
        return lo

    # returns sum(gauss(i)) for 1 <= i <= n
    # this was derived from the regular gauss sum formula (n(n+1)) / 2 = sum of all ints in [1,n]
    def sum_gauss(self, n):
        return 0.5 * ((n * (n + 1) * (2*n + 1)) // 6 + (n * (n + 1)) // 2)

    def gauss(self, n):
        return n * (n + 1) // 2
