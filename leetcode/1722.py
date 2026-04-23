class Solution:
    def minimumHammingDistance(self, source, target, swaps):
        n = len(source)

        dsu = DSU(n)
        for u, v in swaps:
            dsu.union(u, v)

        groups = defaultdict(Counter)
        for i in range(n):
            group = dsu.find(i)
            groups[group][source[i]] += 1
            groups[group][target[i]] -= 1

        return sum(max(cnt, 0) for cnts in groups.values() for cnt in cnts.values())


class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, x):
        while self.reps[x] != x:
            x = self.reps[x]
        return x

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp and self.ranks[ap] > self.ranks[bp]:
            self.ranks[ap] += self.ranks[bp]
            self.reps[bp] = ap
        elif ap != bp:
            self.ranks[bp] += self.ranks[ap]
            self.reps[ap] = bp
