DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])

        seen = set()
        def dfs(r, c, pr=-1, pc=-1):
            seen.add((r, c))

            for dr, dc in DIRS:
                if (r+dr, c+dc) != (pr, pc) and 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] == grid[r][c]:
                    if (r+dr, c+dc) in seen or dfs(r+dr, c+dc, r, c):
                        return True

            return False

        return any((r, c) not in seen and dfs(r, c) for r in range(m) for c in range(n))
