class Solution:
    def check(self, nums):
        return sum(nums[i-1] > nums[i] for i in range(len(nums))) <= 1
