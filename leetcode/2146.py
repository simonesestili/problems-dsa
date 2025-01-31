class Solution:
    def highestRankedKItems(self, grid, pricing, start, k):
        curr, heap, seen = [(0, start[0], start[1])], [], set()
        m, n = len(grid), len(grid[0])
        lo, hi = pricing

        for d, r, c in curr:
            if (r, c) in seen: continue
            if len(heap) < k and lo <= grid[r][c] <= hi:
                heappush(heap, (-d, -grid[r][c], -r, -c))
            elif lo <= grid[r][c] <= hi and self.inv(heap[0]) > (d, grid[r][c], r, c):
                heapreplace(heap, (-d, -grid[r][c], -r, -c))
            seen.add((r, c))
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                dr, dc = dr + r, dc + c
                if dr < 0 or dc < 0 or dr >= m or dc >= n or not grid[dr][dc]:
                    continue
                curr.append((d + 1, dr, dc))

        return [(-r, -c) for d, p, r, c in sorted(heap, reverse=True)]

    def inv(self, x):
        return (-x[0], -x[1], -x[2], -x[3])
