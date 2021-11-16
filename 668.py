class Solution:
    def findKthNumber(self, m, n, k):
        lo, hi = 1, m * n
        while lo < hi:
            cand = (lo + hi) // 2
            if sum(min(cand // row, n) for row in range(1, m + 1)) < k:
                lo = cand + 1
            else:
                hi = cand
        return lo
