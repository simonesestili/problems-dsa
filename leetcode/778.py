DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))
class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        dsu = DSU(n * n)
        heights = {grid[r][c]: (r, c) for r in range(n) for c in range(n)}

        for t in range(n * n):
            r, c = heights[t]
            for R, C in DIRS:
                R, C = r+R, c+C
                if 0 <= R < n and 0 <= C < n and grid[R][C] < t:
                    dsu.union(r*n+c, R*n+C)
            if dsu.find(0) == dsu.find(n*n-1):
                return t

class DSU:
    def __init__(self, n):
        self.ranks = [1] * n
        self.reps = list(range(n))

    def find(self, a):
        while self.reps[a] != a:
            a = self.reps[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if self.ranks[ap] > self.ranks[bp]:
            self.reps[bp] = ap
            self.ranks[ap] += self.ranks[bp]
        else:
            self.reps[ap] = bp
            self.ranks[bp] += self.ranks[ap]
