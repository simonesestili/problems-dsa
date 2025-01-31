class Solution:
    def sumOfDigits(self, nums):
        return 1 ^ (self.total(min(nums)) & 1)

    def total(self, n):
        return sum([int(d) for d in str(n)])
