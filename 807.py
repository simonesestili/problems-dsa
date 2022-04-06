class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        horiz = list(map(max, grid))
        vert = [max(grid[i][j] for i in range(n)) for j in range(n)]

        total = 0
        for row in range(n):
            for col in range(n):
                total += min(horiz[row], vert[col]) - grid[row][col]
        
        return total
