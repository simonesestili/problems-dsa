class Solution:
    def minMoves2(self, nums):
        n, nums = len(nums), sorted(nums)
        return sum(abs(x - nums[n // 2]) for x in nums)
