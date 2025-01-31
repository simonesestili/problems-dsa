class Solution:
    def countOdds(self, lo, hi):
        return (hi - lo) // 2 + bool(lo % 2 or hi % 2)
