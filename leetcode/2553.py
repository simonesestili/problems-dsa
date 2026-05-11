class Solution:
    def separateDigits(self, nums):
        return [int(d) for x in nums for d in str(x)]
