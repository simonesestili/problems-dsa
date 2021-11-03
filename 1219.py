class Solution:
    def getMaximumGold(self, grid):
        m, n = len(grid), len(grid[0])
        gold = 0
        for row in range(m):
            for col in range(n):
                gold = max(gold, self.dfs(grid, row, col, 0))
        return gold        

    def dfs(self, grid, row, col, gold):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or not grid[row][col]:
            return 0
        temp = grid[row][col]
        grid[row][col] = 0
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        for drow, dcol in dirs:
            gold = max(gold, self.dfs(grid, row + drow, col + dcol, gold + temp))
        return temp + gold

