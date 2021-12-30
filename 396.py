class Solution:
    def maxRotateFunction(self, nums):
        n, total = len(nums), sum(nums)
        best = prev = sum(i * v for i, v in enumerate(nums))
        for i in range(1, n):
            prev += total - nums[n - i] * n
            best = max(best, prev)
        return best
