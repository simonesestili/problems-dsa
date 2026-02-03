class Solution:
    def isTrionic(self, nums):
        return [d for d, _ in groupby((1 if nums[i+1] > nums[i] else -1 if nums[i+1] < nums[i] else 0 for i in range(len(nums) - 1)))] == [1, -1, 1]
