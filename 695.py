class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        area = 0

        def explore(i, j):
            if not grid[i][j]: return 0
            grid[i][j] = 0
            res = 1
            for di, dj in DIRS:
                di, dj = i + di, j + dj
                if 0 <= di < m and 0 <= dj < n:
                    res += explore(di, dj)
            return res

        for row in range(m):
            for col in range(n):
                area = max(area, explore(row, col))

        return area
