MOD = 10**9+7
class Solution:
    def numTilings(self, n):
        prev_full = full = 1
        prev_half = half = 0
        for _ in range(n - 1):
            nxt_full = prev_full + full + half
            nxt_half = half + prev_full * 2
            prev_full, full = full, nxt_full % MOD
            prev_half, half = half, nxt_half % MOD
        return full
