class Solution:
    def smallestEquivalentString(self, s1, s2, base):
        dsu, code = DSU(26), lambda c: ord(c) - ord('a')
        for a, b in zip(s1, s2): dsu.union(code(a), code(b))
        return ''.join(chr(ord('a') + min(i for i in range(26) if dsu.find(i) == dsu.find(code(c)))) for c in base)


class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, node):
        while self.reps[node] != node:
            node = self.reps[node]
        return node

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap == bp: return

        if self.ranks[ap] > self.ranks[bp]:
            self.reps[bp] = ap
            self.ranks[ap] += self.ranks[bp]
        else:
            self.reps[ap] = bp
            self.ranks[bp] += self.ranks[ap]
