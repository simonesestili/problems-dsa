class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        for a, b, c in zip(nums, nums[1:], nums[2:]):
            if a < b + c: return a + b + c
        return 0
