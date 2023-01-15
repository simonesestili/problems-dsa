class Solution:
    def smallestEquivalentString(self, s1, s2, base):
        uf, code = UF(26), lambda c: ord(c) - ord('a')
        for a, b in zip(s1, s2): uf.union(code(a), code(b))
        return ''.join((chr(ord('a') + min(i for i in range(26) if uf.find(i) == uf.find(code(c)))) for c in base))

class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp: self.parent[ap] = bp
