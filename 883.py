class Solution:
    def projectionArea(self, grid):
        n = len(grid)
        total = 0
        for row in range(n):
            curr = 0
            for col in range(n):
                total += grid[row][col] > 0
                curr = max(curr, grid[row][col])
            total += curr

        for col in range(n):
            curr = 0 
            for row in range(n):
                curr = max(curr, grid[row][col])
            total += curr

        return total

