DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def numDistinctIslands(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c, orig_r, orig_c, curr):
            curr.append((r - orig_r, c - orig_c))
            grid[r][c] = 0

            for dr, dc in DIRS:
                dr, dc = r + dr, c + dc
                if dr < 0 or dc < 0 or dr >= m or dc >= n or grid[dr][dc] == 0:
                    continue
                dfs(dr, dc, orig_r, orig_c, curr)

        islands = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0: continue
                dfs(row, col, row, col, curr := [])
                islands.add(tuple(curr))

        return len(islands)
