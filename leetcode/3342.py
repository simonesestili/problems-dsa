class Solution:
    def minTimeToReach(self, moveTime):
        m, n = len(moveTime), len(moveTime[0])
        q, seen = [(0, 0, 0, 0)], set([(0, 0)])
        while q:
            t, p, r, c = heappop(q)
            if (r, c) == (m - 1, n - 1):
                return t
            for dr, dc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if 0 <= dr < m and 0 <= dc < n and (dr, dc) not in seen:
                    cost = max(t, moveTime[dr][dc]) + p % 2 + 1
                    heappush(q, (cost, (p + 1) % 2, dr, dc))
                    seen.add((dr, dc))
