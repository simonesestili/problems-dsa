class Solution:
    def findNumbers(self, nums):
        return sum(~len(str(x)) & 1 for x in nums)
