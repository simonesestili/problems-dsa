MOD = 10 ** 9 + 7
class Solution:
    def concatenatedBinary(self, n):
        ans = 0
        for i in range(1, n + 1):
            ans = ((ans << i.bit_length()) + i) % MOD
        return ans
