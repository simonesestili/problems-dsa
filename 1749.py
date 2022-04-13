class Solution:
    def maxAbsoluteSum(self, nums):
        prefix = 0
        mn = mx = 0

        for x in nums:
            prefix += x
            mn, mx = min(mn, prefix), max(mx, prefix)

        return mx - mn
