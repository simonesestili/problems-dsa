class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        return sum(bisect_right(nums, upper - x, hi=i) - bisect_left(nums, lower - x, hi=i) for i, x in enumerate(nums))
