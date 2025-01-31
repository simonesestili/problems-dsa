class Solution:
    def minimumAverageDifference(self, nums):
        ans, best = 0, float('inf')
        left, right = 0, sum(nums)
        for i, x in enumerate(nums):
            left, right = left + x, right - x
            la, ra = left // (i + 1), right // ((len(nums) - i - 1) or 1)
            if abs(la - ra) < best: ans, best = i, abs(la - ra)
        return ans
