class Solution:
    def largestIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def neighs(r, c):
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc]:
                    yield (r+dr, c+dc)

        seen = {}
        def dfs(r, c, idx):
            if (r, c) in seen: return 0
            seen[(r, c)] = idx
            return 1 + sum(dfs(dr, dc, idx) for dr, dc in neighs(r, c))

        sizes, curr = {}, 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r, c) not in seen:
                    sizes[curr] = dfs(r, c, curr)
                    curr += 1

        ans = max(sizes.values(), default=0)
        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    ans = max(ans, 1 + sum(sizes.get(i, 0) for i in set(seen.get((dr, dc), -1) for dr, dc in neighs(r, c))))

        return ans
