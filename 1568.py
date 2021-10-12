class Solution:
    def minDays(self, grid):
        m, n = len(grid), len(grid[0])

        def countIsland(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] <= 0:
                return
            grid[row][col] = -1
            dirs = [[1,0],[-1,0],[0,1],[0,-1]]
            for drow, dcol in dirs:
                countIsland(row + drow, col + dcol)

        def numIslands():
            islands = 0
            for row in range(m):
                for col in range(n):
                    if grid[row][col] > 0:
                        islands += 1
                        countIsland(row, col)
            for row in range(m):
                for col in range(n):
                    grid[row][col] = abs(grid[row][col])
            return islands        

        count = numIslands()
        if count > 1 or count == 0:
            return 0

        # Check if removing any one land disconnects island
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    grid[row][col] = 0
                    count = numIslands()
                    if count > 1 or count == 0:
                        return 1
                    grid[row][col] = 1
                    
        # Otherwise remove 2 because removing 2 will always guarantee disconnection
        return 2
