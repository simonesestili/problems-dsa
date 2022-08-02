class Solution:
    def kthSmallest(self, mat, k):
        lo, hi = -10 ** 9, 10 ** 9
        while lo < hi:
            cand = (lo + hi + 1) // 2
            less = sum(bisect_left(row, cand) for row in mat)
            if less >= k: hi = cand - 1
            else: lo = cand
        return lo
