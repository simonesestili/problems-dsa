class Solution:
    def combinationSum4(self, nums, k):
        nums, dp = sorted(nums), [1] + [0] * k
        for l in range(1, k + 1):
            for x in nums:
                if x > l: break
                dp[l] += dp[l - x]
        return dp[k]
