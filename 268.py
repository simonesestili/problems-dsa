class Solution:
    def missingNumber(self, nums):
        ans = len(nums)
        for i in range(len(nums)):
            ans ^= nums[i] ^ i
        return ans
