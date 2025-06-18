class Solution:
    def maximumDifference(self, nums):
        ans, mn = 0, nums[0]
        for x in nums:
            ans = max(ans, x - mn)
            mn = min(mn, x)
        return ans or -1
