class Solution:
    def findTargetSumWays(self, nums, target):
        n = len(nums)

        @cache
        def dp(i, target):
            if i == n: return int(not target)
            return dp(i + 1, target + nums[i]) + dp(i + 1, target - nums[i])

        return dp(0, target)
