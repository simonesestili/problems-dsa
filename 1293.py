DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def shortestPath(self, grid, k):
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0, k)]) # steps, row, col, rem
        seen = set([(0, 0, k)])

        while queue:
            steps, row, col, rem = queue.popleft()
            if (row, col) == (m - 1, n - 1): return steps
            for dr, dc in DIRS:
                dr, dc = row + dr, col + dc
                if 0 <= dr < m and 0 <= dc < n and rem - grid[dr][dc] >= 0 and (dr, dc, rem - grid[dr][dc]) not in seen:
                    queue.append((steps + 1, dr, dc, rem - grid[dr][dc]))
                    seen.add((dr, dc, rem - grid[dr][dc]))

        return -1
