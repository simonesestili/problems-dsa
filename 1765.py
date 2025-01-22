DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def highestPeak(self, grid):
        m, n, q, seen = len(grid), len(grid[0]), deque(), set()
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    grid[r][c] = 0
                    q.append((r, c, 0))
                    seen.add((r, c))

        while q:
            r, c, h = q.popleft()
            for dr, dc in DIRS:
                dr, dc = r + dr, c + dc
                if 0 <= dr < m and 0 <= dc < n and (dr, dc) not in seen:
                    grid[dr][dc] = h + 1
                    q.append((dr, dc, h + 1))
                    seen.add((dr, dc))

        for r in range(m):
            for c in range(n):
                grid[r][c] = max(grid[r][c], 0)

        return grid
