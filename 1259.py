class Solution:
    def numberOfWays(self, n):
        MOD = pow(10, 9) + 7
        
        @cache
        def dp(n):
            if n & 1 or not n: return 1 if not n else 0
            ans = 0
            for i in range(2, n + 1):
                ans = (ans + dp(i - 2) * dp(n - i) % MOD) % MOD
            return ans

        return dp(n)
