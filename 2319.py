class Solution:
    def checkXMatrix(self, grid):
        n = len(grid)
        for row in range(n):
            for col in range(n):
                if (row == col or row == n-1-col):
                    if not grid[row][col]:
                        return False
                elif grid[row][col]:
                    return False
        return True
