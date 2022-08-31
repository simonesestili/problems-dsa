DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        inbounds = lambda r, c: 0 <= r < m and 0 <= c < n

        def climb(curr):
            seen = set(curr)
            while curr:
                r, c = curr.popleft()
                for R, C in DIRS:
                    R, C = r+R, c+C
                    if not inbounds(R, C) or (R, C) in seen or heights[r][c] > heights[R][C]: continue
                    curr.append((R, C))
                    seen.add((R, C))
            return seen

        P = deque([(r, 0) for r in range(m)] + [(0, c) for c in range(1, n)])
        A = deque([(r, n-1) for r in range(m)] + [(m-1, c) for c in range(n-1)])
        return climb(P) & climb(A)
