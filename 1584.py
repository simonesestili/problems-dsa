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
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points):
        n, edges = len(points), []
        for i, (x, y) in enumerate(points):
            for j in range(i):
                xx, yy = points[j]
                dist = abs(xx - x) + abs(yy - y)
                edges.append((dist, i, j))

        dsu, edges, cost = DSU(n), sorted(edges), 0
        for w, u, v in edges:
            if dsu.union(u, v):
                cost += w
            if dsu.ranks[dsu.find(0)] == n: break
        return cost
