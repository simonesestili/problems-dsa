class Solution:
    def countComponents(self, n, edges):
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        count = set()
        for i in range(n):
            count.add(dsu.find(i))
        return len(count)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a):
        while a != self.parent[a]:
            a = self.parent[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.rank[ap] > self.rank[bp]:
                self.parent[bp] = ap
                self.rank[ap] += self.rank[bp]
            else:
                self.parent[ap] = bp
                self.rank[bp] += self.rank[ap]
