class Solution:
    def subarraySum(self, nums):
        ans = 0
        for i, x in enumerate(nums):
            start = max(0, i - x)
            ans += sum(nums[start:i+1])
        return ans


