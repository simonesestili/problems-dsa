class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        seen = [[[False] * 4  for _ in range(n)] for _ in range(n)]

        def dfs(r, c, q):
            if r < 0 or c < 0 or r >= n or c >= n or seen[r][c][q]: return 0
            seen[r][c][q] = True

            neighs = [(r + (q + 1) % (-2 if q == 0 else 2), c + q % (-2 if q == 3 else 2), (q + 2) % 4)]
            if grid[r][c] != '\\': neighs.append((r, c, 3 - q))
            if grid[r][c] != '/': neighs.append((r, c, 3 - (q + 2) % 4))

            for nr, nc, nq in neighs:
                dfs(nr, nc, nq)
            return 1

        ans = 0
        for i in range(n):
            for j in range(n):
                for q in range(4):
                    ans += dfs(i, j, q)

        return ans

