class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        rots = []
        # Find oranges which are initially rotten
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rots.append((row, col))
        minutes = 0
        while rots:
            next_rots = []
            for row, col in rots:
                dirs = [[1,0], [0,1], [-1,0], [0,-1]]
                for drow, dcol in dirs:
                    drow, dcol = drow + row, dcol + col
                    if drow >= 0 and dcol >= 0 and drow < m and dcol < n and grid[drow][dcol] == 1:
                        grid[drow][dcol] = 2
                        next_rots.append((drow, dcol))
            if next_rots:
                minutes += 1
            rots = next_rots    
        # Make sure all oranges are rotted    
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1
        return minutes        
