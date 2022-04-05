class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        DIRS = ((1,0), (0,1), (-1,0), (0,-1))

        def explore(i, j):
            grid[i][j] = '0'
            for di, dj in DIRS:
                di, dj = i + di, j + dj
                if 0 <= di < m and 0 <= dj < n and grid[di][dj] == '1':
                    explore(di, dj)

        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '0': continue
                explore(row, col)
                ans += 1

        return ans
                
