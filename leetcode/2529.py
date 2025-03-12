class Solution:
    def maximumCount(self, nums):
        return max(bisect_left(nums, 0), len(nums) - bisect_right(nums, 0))
