class Solution:
    def minimumSwaps(self, nums):
        n, mn, mx = len(nums), min(nums), max(nums)
        left = nums.index(mn)
        right = n - 1 - nums[::-1].index(mx)
        return left + (n - 1 - right) - (left > right)
