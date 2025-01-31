class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])
        DIRS = ((1,0), (0,1), (-1,0), (0,-1))

        def dfs(row, col):
            if grid[row][col]: return True
            if row == 0 or col == 0 or row == m - 1 or col == n - 1: return False
            grid[row][col] = 1
            closed = True
            for drow, dcol in DIRS:
                closed &= dfs(drow + row, dcol + col)
            return closed

        return len([0 for j in range(n) for i in range(m) if not grid[i][j] and dfs(i, j)])
