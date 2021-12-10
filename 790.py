class Solution:
    def numTilings(self, n):
        M = 10 ** 9 + 7
        prev_full, full = 1, 1
        prev_half, half = 0, 0
        
        for _ in range(n - 1):
            new_full = prev_full + full + half
            new_half = half + prev_full * 2
            prev_full, full = full, new_full % M
            prev_half, half = half, new_half % M

        return full
