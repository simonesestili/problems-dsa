class Solution:
    def findFinalValue(self, nums, val):
        nums = set(nums)
        while val in nums:
            val *= 2
        return val
