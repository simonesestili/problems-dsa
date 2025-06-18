MOD = 10**9+7
class Solution:
    def countGoodArrays(self, n, m, k):
        return m * pow(m - 1, n - k - 1, MOD) * comb(n - 1, k) % MOD
