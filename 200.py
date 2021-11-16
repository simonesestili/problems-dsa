class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        DIRS = ((1,0), (0,1), (-1,0), (0,-1))

        def explore(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            for drow, dcol in DIRS:
                explore(row + drow, col + dcol)

        count = 0
        for i in range(m):
            for j in range(n):
                count += int(grid[i][j])
                explore(i, j)
        return count
