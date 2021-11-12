class Solution:
    def numEnclaves(self, grid):
        m, n = len(grid), len(grid[0])
        DIRS = [0, 1, 0, -1, 0]

        def explore(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or not grid[row][col]:
                return
            grid[row][col] = 0
            for i in range(4):
                explore(row + DIRS[i], col + DIRS[i + 1])

        for i in range(m):
            explore(i, 0)
            explore(i, n - 1)
        for j in range(n):
            explore(0, j)
            explore(m - 1, j)

        count = 0
        for row in range(m):
            for col in range(n):
                count += grid[row][col]
        return count
