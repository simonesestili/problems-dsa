DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def trapRainWater(self, grid):
        m, n, q = len(grid), len(grid[0]), []
        for r in range(m):
            for c in range(n):
                if r in (0, m-1) or c in (0, n-1):
                    heappush(q, (grid[r][c], r, c))
                    grid[r][c] = -1

        ans = 0
        while q:
            h, r, c = heappop(q)
            for dr, dc in DIRS:
                if 0 < r+dr < m - 1 and 0 < c+dc < n - 1 and grid[r+dr][c+dc] != -1:
                    ans += max(h - grid[r+dr][c+dc], 0)
                    heappush(q, (max(h, grid[r+dr][c+dc]), r+dr, c+dc))
                    grid[r+dr][c+dc] = -1

        return ans
