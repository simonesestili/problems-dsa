class Solution:
    def equationsPossible(self, eqs):
        dsu = DSU(26)
        code = lambda c: ord(c) - ord('a')
        parse = lambda x: (code(x[:1]), x[1:2], code(x[3:]))
        
        for x, op, y in map(parse, eqs):
            if op == '=': dsu.union(x, y)

        return not any(dsu.find(x) == dsu.find(y) for x, op, y in map(parse, eqs) if op == '!')

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a):
        while self.parent[a] != a:
            a = self.parent[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap == bp: return
        if self.rank[ap] > self.rank[bp]:
            self.parent[bp] = ap
            self.rank[ap] += self.rank[bp]
        else:
            self.parent[ap] = bp
            self.rank[bp] += self.rank[ap]
