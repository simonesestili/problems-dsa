class Solution:
    def maximumBags(self, cap, rocks, extra):
        ans = 0
        for rem in sorted(c - r for c, r in zip(cap, rocks)):
            x = min(rem, extra)
            extra, rem = extra - x, rem - x
            if rem: break
            ans += 1

        return ans
