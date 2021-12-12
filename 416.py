class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2: return False
        n = len(nums)

        @lru_cache(None)
        def dp(idx, rem):
            if rem <= 0: return not rem
            if idx == n: return False
            return dp(idx + 1, rem) or dp(idx + 1, rem - nums[idx])

        return dp(0, sum(nums) // 2)
