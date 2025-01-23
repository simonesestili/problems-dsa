class Solution:
    def countServers(self, grid):
        m, n = len(grid), len(grid[0])
        rows, cols = [0] * m, [0] * n

        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    rows[r] += 1
                    cols[c] += 1

        return sum(max(rows[r], cols[c]) > 1 for c in range(n) for r in range(m) if grid[r][c])
