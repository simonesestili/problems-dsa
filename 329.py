DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def longestIncreasingPath(self, mat):
        m, n = len(mat), len(mat[0])

        @cache
        def dp(row, col):
            best = 1
            for drow, dcol in DIRS:
                drow, dcol = row + drow, col + dcol
                if drow < 0 or dcol < 0 or drow >= m or dcol >= n or mat[drow][dcol] <= mat[row][col]:
                    continue
                best = max(best, 1 + dp(drow, dcol))
            return best

        return max(dp(row, col) for col in range(n) for row in range(m))
