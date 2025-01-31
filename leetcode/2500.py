class Solution:
    def deleteGreatestValue(self, grid):
        m, n = len(grid), len(grid[0])
        for row in grid: row.sort()

        ans = 0
        for col in range(n):
            ans += max(grid[row][col] for row in range(m))

        return ans
