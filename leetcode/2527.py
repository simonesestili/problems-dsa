class Solution:
    def xorBeauty(self, nums):
        return reduce(xor, nums)
