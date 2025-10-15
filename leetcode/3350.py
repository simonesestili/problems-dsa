class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        left, right = [1] * n, [1] * n
        for i in range(n - 1):
            left[i+1] += left[i] if nums[i] < nums[i+1] else 0
            right[n-i-2] += right[n-i-1] if nums[n-i-2] < nums[n-i-1] else 0
        return max(min(left[i], right[i+1]) for i in range(n - 1))
