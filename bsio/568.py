class Solution:
    def solve(self, nums):
        n = len(nums)

        @cache
        def dp(i):
            if i == n: return True
            if i > n: return False
            a, b, c = nums[i], None if i == n - 1 else nums[i+1], None if i >= n - 2 else nums[i+2]
            if a == b and dp(i + 2): return True
            if a == b == c and dp(i + 3): return True
            if a + 1 == b and b + 1 == c and dp(i + 3): return True
            return False

        return dp(0)
