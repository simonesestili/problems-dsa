class Solution:
    def maxStability(self, n, edges, k):
        must = [(s, u, v) for u, v, s, m in edges if m]
        other = sorted([(s, u, v) for u, v, s, m in edges if not m], reverse=True)

        mn, dsu = inf, DSU(n)
        for s, u, v in must:
            if dsu.find(u) == dsu.find(v):
                return -1
            dsu.union(u, v)
            mn = min(mn, s)

        cands = []
        for s, u, v in other:
            if dsu.find(u) == dsu.find(v):
                continue
            dsu.union(u, v)
            cands.append(s)

        if dsu.ranks[dsu.find(0)] != n:
            return -1

        for _ in range(min(k, len(cands))):
            mn = min(mn, cands.pop() * 2)

        if cands:
            mn = min(mn, cands[-1])

        return mn

class DSU:
    def __init__(self, n) -> None:
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, x):
        while self.reps[x] != x:
            x = self.reps[x]
        return x

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if self.ranks[ap] > self.ranks[bp]:
            self.reps[bp] = ap
            self.ranks[ap] += self.ranks[bp]
        else:
            self.reps[ap] = bp
            self.ranks[bp] += self.ranks[ap]
