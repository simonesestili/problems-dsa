class Solution:
    def minOperations(self, nums):
        ans = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                ans += 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
        return ans if nums[-2] and nums[-1] else -1
