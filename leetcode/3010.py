class Solution:
    def minimumCost(self, nums):
        return nums[0] + sum(nsmallest(2, nums[1:]))
