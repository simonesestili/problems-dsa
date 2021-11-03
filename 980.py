class Solution:
    def uniquePathsIII(self, grid):
        self.ans = 0
        row1 = col1 = row2 = col2 = remaining = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    row1, col1 = row, col
                elif grid[row][col] == 2:
                    row2, col2 = row, col
                if grid[row][col] == 0 or grid[row][col] == 1:
                    remaining += 1

        def dfs(row, col, rem):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] < 0:
                return
            if row == row2 and col == col2:
                self.ans += rem == 0
                
            grid[row][col] = -1
            dirs = [[1,0],[0,1],[-1,0],[0,-1]]
            for drow, dcol in dirs:
                dfs(row + drow, col + dcol, rem - 1)
            grid[row][col] = 0    

        dfs(row1, col1, remaining)
        return self.ans
