class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    perimeter += self.perimeter(grid, row, col)
        return perimeter            

    def perimeter(self, grid, row, col):
        diffs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        perimeter = 0
        for diff in diffs:
            drow, dcol = row + diff[0], col + diff[1]
            if drow < 0 or dcol < 0 or drow >= len(grid) or dcol >= len(grid[0]) or not grid[drow][dcol]:
                perimeter += 1
        return perimeter        
