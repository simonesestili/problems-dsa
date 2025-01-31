MOD = 10 ** 9 + 7
DIRS = ((1,0), (0,1), (-1,0), (0,-1))
class Solution:
    def findPaths(self, m, n, moves, startRow, startCol):
        inbounds = lambda r, c: 0 <= r < m and 0 <= c < n

        @cache
        def ways(row, col, k):
            if not inbounds(row, col): return 1
            if k == 0: return 0
            return sum(ways(row + dr, col + dc, k - 1) for dr, dc in DIRS) % MOD

        return ways(startRow, startCol, moves)
