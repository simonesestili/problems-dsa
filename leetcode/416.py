class Solution:
    def canPartition(self, nums):
        n, total = len(nums), sum(nums)
        if total % 2: return False

        @cache
        def dp(i, rem):
            if rem <= 0: return rem == 0
            if i >= n: return False
            return dp(i + 1, rem) or dp(i + 1, rem - nums[i])

        return dp(0, total // 2)
