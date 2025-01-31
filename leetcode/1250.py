class Solution:
    def isGoodArray(self, nums):
        gcd = nums[0]
        for num in nums:
            gcd = self.gcd(gcd, num)
        return gcd == 1

    def gcd(self, a, b):
        if not a:
            return b
        return self.gcd(b % a, a)
