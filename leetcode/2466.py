MOD = 10**9 + 7
class Solution:
    def countGoodStrings(self, lo, hi, a, b):

        @cache
        def dp(i):
            if i < 0: return 0
            if i == 0: return 1
            return (dp(i - a) + dp(i - b)) % MOD

        return sum(dp(i) for i in range(lo, hi + 1)) % MOD
