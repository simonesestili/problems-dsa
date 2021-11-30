class DSU:
    def __init__(self):
        self.reps = {}
        self.ranks = {}

    def find(self, node):
        if node not in self.reps:
            self.reps[node] = node
        while node != self.reps[node]:
            node = self.reps[node]
        return node

    def union(self, a, b):
        if a not in self.reps:
            self.reps[a], self.ranks[a] = a, 1
        if b not in self.reps:
            self.reps[b], self.ranks[b] = b, 1
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.reps[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.reps[ap] = bp
                self.ranks[bp] += self.ranks[ap]

class Solution:
    def findAllPeople(self, n, meetings, first):
        know = [False] * n
        know[0], know[first] = True, True
        meets = defaultdict(list)
        for x, y, t in meetings:
            meets[t].append((x, y))
        times = sorted(meets.keys())
        for time in times:
            seen, uf = set(), DSU()
            for x, y in meets[time]:
                if know[x] and know[y]:
                    continue
                if know[x] or know[y]:
                    seen.add(x)
                uf.union(x, y)

            secrets = set()
            for p in seen:
                secrets.add(uf.find(p))
            for x, y in meets[time]:
                if uf.find(x) in secrets:
                    know[x], know[y] = True, True
        return [i for i in range(n) if know[i]]
