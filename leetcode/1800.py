class Solution:
    def maxAscendingSum(self, nums):
        ans = curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: curr += nums[i]
            else: curr = nums[i]
            ans = max(ans, curr)
        return ans
