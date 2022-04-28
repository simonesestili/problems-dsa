DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])

        def reachable(effort):
            seen = set()
            dfs(0, 0, effort, seen)
            return (m - 1, n - 1) in seen

        def dfs(i, j, effort, seen):
            h = heights[i][j]
            seen.add((i, j))
            for di, dj in DIRS:
                di, dj = i + di, j + dj
                if di < 0 or dj < 0 or di >= m or dj >= n: continue
                if (di, dj) in seen or abs(heights[di][dj] - h) > effort: continue
                dfs(di, dj, effort, seen)

        lo, hi = 0, max(map(max, heights)) - min(map(min, heights))
        while lo < hi:
            cand = (lo + hi) // 2
            if reachable(cand): hi = cand
            else: lo = cand + 1

        return lo
