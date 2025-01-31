class Solution:
    def countGoodNumbers(self, n):
        MOD = 10 ** 9 + 7
        evens, odds = n - n // 2, n // 2
        return pow(5, evens, MOD) * pow(4, odds, MOD) % MOD
