class Solution:
    def colorBorder(self, grid, r, c, color):
        DIRS = ((1,0), (0,1), (-1,0), (0,-1))
        m, n = len(grid), len(grid[0])
        target = grid[r][c]
        
        def is_border(row, col):
            if not row or not col or row + 1 == m or col + 1 == n:
                return True
            for drow, dcol in DIRS:
                val = abs(grid[row + drow][col + dcol])
                if val and val != target:
                    return True
            return False

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] != target:
                return
            # check if it is a border
            if is_border(row, col):
                grid[row][col] = 0
            grid[row][col] *= -1 # mark as visited
            for drow, dcol in DIRS:
                dfs(row + drow, col + dcol)

        dfs(r, c)
        return [[abs(x) if x else color for x in row] for row in grid]
