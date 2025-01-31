DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def minDays(self, grid):
        m, n = len(grid), len(grid[0])
        
        def count_islands():
            seen = set()
            def dfs(r, c):
                if not grid[r][c] or (r, c) in seen: return 0
                seen.add((r, c))
                for dr, dc in DIRS:
                    if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc]:
                        dfs(r + dr, c + dc)
                return 1
            return sum(dfs(i, j) for j in range(n) for i in range(m))

        if count_islands() != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if not grid[i][j]: continue
                grid[i][j] = 0
                if count_islands() != 1: return 1
                grid[i][j] = 1

        return 2

