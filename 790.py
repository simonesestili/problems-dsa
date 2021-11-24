class Solution:
    def numTilings(self, n):
        MOD = 10 ** 9 + 7
        full, half = [1, 1], [0, 0]
        for _ in range(n - 1):
            new_full, new_half = full[0] + full[1] + half[1], half[1] + 2 * full[0]
            full, half = [full[1], new_full % MOD], [half[1], new_half % MOD]
        return full[1]
