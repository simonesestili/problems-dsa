class Solution:
    def solve(self, points, k):
        n = len(points)
        dsu = DSU(n)
        for i, (x, y) in enumerate(points):
            for j, (xx, yy) in enumerate(points[:i]):
                if pow(xx - x, 2) + pow(yy - y, 2) <= k * k:
                    dsu.union(i, j)
        return len(set(dsu.find(i) for i in range(n)))

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


