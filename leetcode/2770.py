class Solution:
    def maximumJumps(self, nums, target):
        n = len(nums)
        dp = [0] + [-inf] * (n-1)
        for i in range(1, n):
            for j in range(i):
                if abs(nums[i]-nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp[-1], -1)
