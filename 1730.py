class Solution:
    def getFood(self, grid):
        start = (-1, -1)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    start = (i, j)

        queue, seen = deque([(start[0], start[1], 0)]), set([start])
        while queue:
            r, c, steps = queue.popleft()
            if grid[r][c] == '#': return steps
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dr, dc = r + dr, c + dc
                if 0 <= dr < m and 0 <= dc < n and (dr, dc) not in seen and grid[dr][dc] != 'X':
                    queue.append((dr, dc, steps + 1))
                    seen.add((dr, dc))

        return -1
