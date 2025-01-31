class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        @cache
        def dp(left, right):
            best = 0
            for k in range(left, right + 1):
                best = max(best, nums[left - 1] * nums[k] * nums[right + 1] + dp(left, k - 1) + dp(k + 1, right))
            return best

        return dp(1, n - 2)
