class Solution:
    def numOfArrays(self, n, m, k):
        MOD = pow(10, 9) + 7

        @cache
        def dp(l, mx, s):
            if l == 1: return int(s == 1)
            if s == 0: return 0

            ans = dp(l - 1, mx, s) * mx % MOD
            ans += sum(dp(l - 1, num, s - 1) for num in range(1, mx))

            return ans % MOD

        return sum(dp(n, i, k) for i in range(1, m + 1)) % MOD
