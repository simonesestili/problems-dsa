class Solution:
    def subsetXORSum(self, nums):
        return reduce(lambda a, b: a | b, nums) << (len(nums) - 1)
