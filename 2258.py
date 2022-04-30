DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def maximumMinutes(self, grid):
        m, n = len(grid), len(grid[0])
        fires = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                fires.append((i, j, 0))

        burns = {}
        while fires:
            i, j, t = fires.popleft()
            if (i, j) in burns: continue
            burns[(i, j)] = t
            for di, dj in DIRS:
                di, dj = i + di, j + dj
                if di < 0 or dj < 0 or di >= m or dj >= n or grid[di][dj] != 0: continue
                fires.append((di, dj, t + 1))

        def reachable(time, seen, row=0, col=0):
            if (row, col) in seen or burns.get((row, col), float('inf')) <= time and (row, col) != (m-1, n-1): return False
            if (row, col) == (m-1, n-1): return burns.get((row, col), float('inf')) >= time
            seen.add((row, col))
            for dr, dc in DIRS:
                dr, dc = row + dr, col + dc
                if dr < 0 or dc < 0 or dr >= m or dc >= n or grid[dr][dc] == 2: continue
                if reachable(time + 1, seen, dr, dc): return True
            return False

        lo, hi = 0, 10 ** 9
        while lo < hi:
            cand = (lo + hi + 1) // 2
            if reachable(cand, set()): lo = cand
            else: hi = cand - 1
        return lo if lo else lo if reachable(lo, set()) else -1
