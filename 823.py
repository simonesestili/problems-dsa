MOD = 10 ** 9 + 7
class Solution:
    def numFactoredBinaryTrees(self, nums):
        nums = sorted(nums)
        seen = set(nums)

        @cache
        def dp(product):
            ans = 1
            for f1 in nums:
                f2 = product // f1
                if f1 * f1 > product: break
                if product % f1 or f2 not in seen: continue
                d = 1 + (f1 != f2)
                ans = (ans + dp(f1) * dp(f2) * d) % MOD
            return ans

        return sum(dp(x) for x in nums) % MOD
