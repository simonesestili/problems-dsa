class Solution:
    def findPaths(self, m, n, moves, startRow, startCol):
        MOD = 10 ** 9 + 7
        DIRS = ((1,0), (0,1), (-1,0), (0,-1))
        
        @lru_cache(None)
        def ways(row, col, k):
            if row < 0 or col < 0 or row >= m or col >= n:
                return 1
            if k == 0: return 0
            ans = 0
            for drow, dcol in DIRS:
                ans += ways(row + drow, col + dcol, k - 1) % MOD
            return ans

        return ways(startRow, startCol, moves) % MOD
