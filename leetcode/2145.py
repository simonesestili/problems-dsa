class Solution:
    def numberOfArrays(self, diffs, lo, hi):
        curr = mn = mx = 0
        for d in diffs:
            curr += d
            mn = min(mn, curr)
            mx = max(mx, curr)
        return max((hi - lo) - (mx - mn) + 1, 0)
