class Solution:
    # BFS from initially rotten oranges
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        rots = []
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rots.append((row, col))
        minutes = 0
        while rots:
            new_rots = []
            for row, col in rots:
                dirs = [[1,0], [0,1], [-1,0], [0,-1]] 
                for drow, dcol in dirs:
                    drow, dcol = row + drow, col + dcol
                    if drow >= 0 and dcol >= 0 and drow < m and dcol < n and grid[drow][dcol] == 1:
                        grid[drow][dcol] = 2
                        new_rots.append((drow, dcol))
            if new_rots:
                minutes += 1
            rots = new_rots
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1
        return minutes        
