class Solution:
    def surfaceArea(self, grid):
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        area, n = 0, len(grid)

        def get(i, j):
            if i < 0 or i >= n or j < 0 or j >= n: return 0
            return grid[i][j]

        for row in range(n):
            for col in range(n):
                area += 2 if grid[row][col] else 0
                for dr, dc in DIRS:
                    area += max(grid[row][col] - get(row + dr, col + dc), 0)

        return area
