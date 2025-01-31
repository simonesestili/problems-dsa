DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def maxPoints(self, grid, queries):
        m, n, k = len(grid), len(grid[0]), len(queries)
        ans, heap, seen = [0] * k, [(grid[0][0], 0, 0)], set([(0, 0)])

        spread = 0
        for q, idx in sorted((q, i) for i, q in enumerate(queries)):
            while heap and q > heap[0][0]:
                _, row, col = heappop(heap)
                spread += 1
                for dr, dc in DIRS:
                    dr, dc = row + dr, col + dc
                    if dr < 0 or dc < 0 or dr >= m or dc >= n or (dr, dc) in seen: continue
                    heappush(heap, (grid[dr][dc], dr, dc))
                    seen.add((dr, dc))
            ans[idx] = spread

        return ans
