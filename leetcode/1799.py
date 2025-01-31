class Solution:
    def maxScore(self, nums):
        n = len(nums)
        
        @cache
        def dp(mask, i):
            if not mask: return 0
            best = 0
            for a in range(0, n - 1):
                for b in range(a + 1, n):
                    choice = (1 << a) + (1 << b)
                    if choice & mask == choice:
                        best = max(best, i * gcd(nums[a], nums[b]) + dp(mask - choice, i + 1))
            return best

        return dp((1 << n) - 1, 1)
