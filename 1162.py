class Solution:
    def maxDistance(self, grid):
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
        n, seen, queue = len(grid), set(), deque()

        for i in range(n):
            for j in range(n):
                if not grid[i][j]: continue
                queue.append((i, j, 0))
                seen.add((i, j))

        ans = -1
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in DIRS:
                dr, dc = r + dr, c + dc
                if (dr, dc) not in seen and 0 <= dr < n and 0 <= dc < n:
                    ans = max(ans, dist + 1)
                    queue.append((dr, dc, dist + 1))
                    seen.add((dr, dc))

        return ans

