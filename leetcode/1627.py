class Solution:
    def areConnected(self, n, threshold, queries):
        dsu = DSU(n + 1)
        for j in range(threshold + 1, n + 1):
            for k in range(j, n + 1, j):
                dsu.union(j, k)
        return [dsu.find(a) == dsu.find(b) for a, b in queries]

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.ranks = [1] * n

    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]
        return node

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.parent[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.parent[ap] = bp
                self.ranks[bp] += self.ranks[ap]
