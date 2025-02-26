class Solution:
    def maxAbsoluteSum(self, nums):
        curr = mn = mx = 0
        for x in nums:
            curr += x
            mn = min(mn, curr)
            mx = max(mx, curr)
        return mx - mn
