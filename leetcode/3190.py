class Solution:
    def minimumOperations(self, nums):
        return sum(x % 3 != 0 for x in nums)
