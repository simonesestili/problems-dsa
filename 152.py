class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        prefix, suffix = nums.copy(), nums.copy()
        for i in range(1, n):
            prefix[i] *= prefix[i - 1] or 1
            suffix[n - 1 - i] *= suffix[n - i] or 1
        return max(prefix + suffix)
