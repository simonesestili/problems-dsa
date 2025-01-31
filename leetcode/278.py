class Solution:
    def firstBadVersion(self, n):
        lo, hi = 1, n
        while lo < hi:
            cand = (lo + hi) // 2
            if isBadVersion(cand):
                hi = cand
            else:
                lo = cand + 1
        return lo
