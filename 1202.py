class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        dsu = DSU(n)
        for a, b in pairs:
            dsu.union(a, b)

        groups = defaultdict(list)
        for i, c in enumerate(s):
            groups[dsu.find(i)].append(c)

        for group in groups:
            groups[group] = sorted(groups[group], reverse=1)

        ans = []
        for i in range(n):
            ans.append(groups[dsu.find(i)].pop())
        return ''.join(ans)

class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, a):
        while a != self.reps[a]:
            a = self.reps[a]
        return a

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.reps[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.reps[ap] = bp
                self.ranks[bp] += self.ranks[ap]
