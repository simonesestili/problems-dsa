DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def uniquePathsIII(self, grid):
        m, n = len(grid), len(grid[0])
        start = next((r, c) for r in range(m) for c in range(n) if grid[r][c] == 1)
        dest = next((r, c) for r in range(m) for c in range(n) if grid[r][c] == 2)
        squares = sum(grid[r][c] != -1 for r in range(m) for c in range(n))

        visitable = lambda r, c: 0 <= r < m and 0 <= c < n and grid[r][c] != -1
        def dfs(row, col, rem):
            if (row, col) == dest: return rem == 0
            grid[row][col] = -1
            ans = sum(dfs(row + dr, col + dc, rem - 1) for dr, dc in DIRS if visitable(row + dr, col + dc))
            grid[row][col] = 1
            return ans

        return dfs(*start, squares - 1)
