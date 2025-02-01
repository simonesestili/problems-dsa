class Solution:
    def isArraySpecial(self, nums):
        return all((nums[i] ^ nums[i-1]) & 1 for i in range(1, len(nums)))
