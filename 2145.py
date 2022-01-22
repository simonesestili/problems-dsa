class Solution:
    def numberOfArrays(self, differences, lo, hi):
        curr = mn = mx = 0
        for d in differences:
            curr += d
            mn, mx = min(mn, curr), max(mx, curr)

        return max(hi - lo - mx + mn + 1, 0)
