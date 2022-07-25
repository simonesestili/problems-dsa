class Solution:
    def searchRange(self, nums, target):
        i, j = bisect_left(nums, target), bisect_right(nums, target) - 1
        return [-1, -1] if i >= len(nums) or nums[i] != target else [i, j]
