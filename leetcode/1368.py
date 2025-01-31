DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))
class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])

        q, seen = deque([(0, 0, 0)]), defaultdict(lambda: inf, {(0, 0): 0})
        while q:
            r, c, cost = q.popleft()
            if (r, c) == (m - 1, n - 1):
                return cost

            for i, (dr, dc) in enumerate(DIRS):
                ncost = cost + int(i + 1 != grid[r][c])
                if ncost >= seen[(r+dr, c+dc)] or r+dr < 0 or r+dr >= m or c+dc < 0 or c+dc >= n:
                    continue
                seen[(r+dr, c+dc)] = ncost
                if cost == ncost:
                    q.appendleft((r+dr, c+dc, ncost))
                else:
                    q.append((r+dr, c+dc, ncost))
