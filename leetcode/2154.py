class Solution:
    def findFinalValue(self, nums, original):
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
