class Solution:
    def numSimilarGroups(self, strs):
        n = len(strs)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i):
                if sum(a != b for a, b in zip(strs[i], strs[j])) > 2:
                    continue
                dsu.union(i, j)
        return len({dsu.find(i) for i in range(n)})

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
        if ap == bp: return False
        if self.ranks[ap] > self.ranks[bp]:
            self.reps[bp] = ap
            self.ranks[ap] += self.ranks[bp]
        else:
            self.reps[ap] = bp
            self.ranks[bp] += self.ranks[ap]
        return True

