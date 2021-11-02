class Solution:
    def getMaximumGold(self, grid):
        DIRS = [0,1,0,-1,0]
        m, n = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or not grid[row][col]:
                return 0
            best = 0
            temp = grid[row][col]
            grid[row][col] = 0
            for i in range(4):
                best = max(best, dfs(row + DIRS[i], col + DIRS[i + 1]))
            grid[row][col] = temp
            return best + temp

        most_gold = 0
        for row in range(m):
            for col in range(n):
                most_gold = max(most_gold, dfs(row, col))
        return most_gold        
                
