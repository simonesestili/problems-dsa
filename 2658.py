class Solution:
    def findMaxFish(self, grid):
        m, n = len(grid), len(grid[0])

        def neighs(r, c):
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] > 0:
                    yield (r+dr, c+dc)

        seen = set()
        def dfs(r, c):
            if (r, c) in seen or grid[r][c] == 0: return 0
            seen.add((r, c))
            return grid[r][c] + sum(dfs(dr, dc) for dr, dc in neighs(r, c))

        return max((dfs(r, c) for c in range(n) for r in range(m)), default=0)
