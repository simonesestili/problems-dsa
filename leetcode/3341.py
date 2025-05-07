DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def minTimeToReach(self, moveTime):
        m, n = len(moveTime), len(moveTime[0])
        q, times = [(0, 0, 0)], defaultdict(lambda: inf, {(0, 0): 0})
        while q:
            t, r, c = heappop(q)
            if (r, c) == (m - 1, n - 1):
                return t
            for dr, dc in DIRS:
                if 0 <= r+dr < m and 0 <= c+dc < n:
                    cost = max(t, moveTime[r+dr][c+dc]) + 1
                    if cost < times[(r+dr, c+dc)]:
                        heappush(q, (cost, r+dr, c+dc))
                        times[(r+dr, c+dc)] = cost
