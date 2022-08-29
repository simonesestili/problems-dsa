DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        inbounds = lambda (i, j): 0 <= i < m and 0 <= j < n

        def sink(i, j):
            if not inbounds(i, j) or grid[i][j] == '0': return
            grid[i][j] = '0'
            for I, J in DIRS: sink(i + I, j + J)

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += grid[i][j] == '1'
                sink(i, j)
        return ans
