class Solution:
    def removeStones(self, stones):
        dsu = DSU(len(stones))
        rows, cols = {}, {}
        for i, (x, y) in enumerate(stones):
            if x not in rows: rows[x] = i
            if y not in cols: cols[y] = i
            dsu.union(i, rows[x])
            dsu.union(i, cols[y])
        return len(stones) - dsu.count

class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n
        self.count = n

    def find(self, a):
        while a != self.reps[a]:
            a = self.reps[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            self.count -= 1
            if self.ranks[ap] > self.ranks[bp]:
                self.reps[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.reps[ap] = bp
                self.ranks[bp] += self.ranks[ap]
