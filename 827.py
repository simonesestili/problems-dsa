DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

class Solution:
    def largestIsland(self, grid):
        n, ans = len(grid), 1
        dsu, idx = DSU(n*n), lambda r, c: r * n + c
        for i in range(n):
            for j in range(n):
                if not grid[i][j]: continue
                for di, dj in DIRS:
                    di, dj = i + di, j + dj
                    if di < 0 or dj < 0 or di >= n or dj >= n or not grid[di][dj]: continue
                    dsu.union(idx(i, j), idx(di, dj))
                    ans = max(ans, dsu.ranks[dsu.find(idx(i, j))])

        for i in range(n):
            for j in range(n):
                if grid[i][j]: continue
                cands = set()
                for di, dj in DIRS:
                    di, dj = i + di, j + dj
                    if di < 0 or dj < 0 or di >= n or dj >= n or not grid[di][dj]: continue
                    cands.add(dsu.find(idx(di, dj)))
                ans = max(ans, 1 + sum(dsu.ranks[p] for p in cands))
        return ans

class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, a):
        while a != self.reps[a]:
            a = self.reps[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.reps[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.reps[ap] = bp
                self.ranks[bp] += self.ranks[ap]

