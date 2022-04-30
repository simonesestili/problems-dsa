class Solution:
    def minimumAverageDifference(self, nums):
        n = len(nums)
        ans, best = 0, float('inf')
        prefix, suffix = 0, sum(nums)
        for i in range(n):
            prefix += nums[i]
            suffix -= nums[i]
            diff = abs(prefix // (i + 1) - (0 if i == n - 1 else suffix // (n - i - 1)))
            if diff < best:
                ans, best = i, diff
        return ans
