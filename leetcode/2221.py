class Solution:
    def triangularSum(self, nums):
        n = len(nums)
        return sum(nums[i] * comb(n - 1, i) for i in range(n)) % 10
