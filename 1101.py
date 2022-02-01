class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.ranks = [1] * n
        self.largest = 1

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.parent[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.parent[ap] = bp
                self.ranks[bp] += self.ranks[ap]
        self.largest = max(self.largest, self.ranks[ap], self.ranks[bp])

class Solution:
    def earliestAcq(self, logs, n):
        dsu, logs = DSU(n), sorted(logs)
        for t, x, y in logs:
            dsu.union(x, y)
            if dsu.largest == n:
                return t
        return -1
