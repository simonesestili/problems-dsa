DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])

        heap, seen = [(0, 0, 0)], set([(0, 0)])
        while heap:
            cost, row, col = heappop(heap)
            if (row, col) == (m - 1, n - 1):
                return cost

            for dr, dc in DIRS:
                dr, dc = row + dr, col + dc
                if dr < 0 or dc < 0 or dr >= m or dc >= n or (dr, dc) in seen:
                    continue
                heappush(heap, (cost + grid[dr][dc], dr, dc))
                seen.add((dr, dc))

        return -1
