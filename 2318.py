MOD = 10 ** 9 + 7
ROLLS = ((1,2,3,4,5,6), (2,3,4,5,6), (1,3,5), (1,2,4,5), (1,3,5), (1,2,3,4,6), (1, 5))
class Solution:
    def distinctSequences(self, n):

        @cache
        def dp(pp, p, i):
            if i == n: return 1
            ans = 0
            for roll in ROLLS[p]:
                if roll == pp: continue
                ans = (ans + dp(p, roll, i + 1)) % MOD
            return ans

        return dp(0, 0, 0)
