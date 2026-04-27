LEFT = ((0, -1), {1, 4, 6})
RIGHT = ((0, 1), {1, 3, 5})
UP = ((-1, 0), {2, 3, 4})
DOWN = ((1, 0), {2, 5, 6})
DIRS = {1: (LEFT, RIGHT), 2: (UP, DOWN), 3: (LEFT, DOWN), 4: (RIGHT, DOWN), 5: (LEFT, UP), 6: (UP, RIGHT)}
class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        seen = set()
        def dfs(r, c):
            seen.add((r, c))
            if (r, c) == (m-1, n-1):
                return True
            for (dr, dc), valids in DIRS[grid[r][c]]:
                dr, dc = r+dr, c+dc
                if 0 <= dr < m and 0 <= dc < n and (dr, dc) not in seen and grid[dr][dc] in valids and dfs(dr, dc):
                    return True
            return False

        return dfs(0, 0)
