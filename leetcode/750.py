class Solution:
    def countCornerRectangles(self, grid):
        m, n, count = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(i):
                prev = 0
                for k in range(m):
                    if not grid[k][i] or not grid[k][j]: continue
                    count += prev
                    prev += 1
        return count
