class Solution:
    def findBall(self, grid):
        m, n = len(grid), len(grid[0])

        ans = [-1] * n
        is_stuck = lambda r, c: c==n-1 or grid[r][c+1] == -1 if grid[r][c] == 1 else c==0 or grid[r][c-1] == 1
        def drop(row, col, ball_id):
            if row == m or is_stuck(row, col):
                ans[ball_id] = col if row == m else -1
                return
            drop(row + 1, col + grid[row][col], ball_id)

        for ball in range(n): drop(0, ball, ball)
        return ans
