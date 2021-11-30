class Solution:
    def knightProbability(self, n, k, row, col):
        DIRS = ((-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2))

        @lru_cache(None)
        def prob(row, col, rem):
            if row < 0 or col < 0 or row >= n or col >= n:
                return 0
            if not rem:
                return 1
            tot = 0
            for drow, dcol in DIRS:
                tot += prob(row + drow, col + dcol, rem - 1) / 8
            return tot

        return prob(row, col, k)
