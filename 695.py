DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        valid = lambda r, c: 0 <= r < m and 0 <= c < n

        def get_area(row, col):
            if not valid(row, col) or not grid[row][col]: return 0
            grid[row][col] = 0 # mark as visited
            return 1 + sum(get_area(dr + row, dc + col) for dr, dc in DIRS)
        
        return max(get_area(i, j) for i in range(m) for j in range(n))


