DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        inbounds = lambda r, c: 0 <= r < m and 0 <= c < n

        def dfs(r, c, seen):
            for R, C in DIRS:
                R, C = r+R, c+C
                if inbounds(R, C) and (R, C) not in seen and heights[R][C] >= heights[r][c]:
                    seen.add((R, C))
                    dfs(R, C, seen)

        p = set()
        for r, c in [(r, 0) for r in range(m)] + [(0, c) for c in range(1, n)]:
            p.add((r, c))
            dfs(r, c, p)
        a = set()
        for r, c in [(r, n-1) for r in range(m)] + [(m-1, c) for c in range(n-1)]:
            a.add((r, c))
            dfs(r, c, a)

        return list(p & a)
