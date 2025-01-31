class Solution:
    def sumSubseqWidths(self, nums):
        total, nums, M, n = 0, sorted(nums), pow(10, 9) + 7, len(nums)
        for i in range(n):
            total = (total + pow(2, i, M) * nums[i]) % M
            total = (total - pow(2, n - 1 - i, M) * nums[i]) % M
        return total
