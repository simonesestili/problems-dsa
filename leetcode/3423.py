class Solution:
    def maxAdjacentDistance(self, nums):
        return max(abs(nums[i] - nums[(i+1)%len(nums)]) for i in range(len(nums)))
