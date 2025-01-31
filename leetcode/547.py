class Solution:
    def findCircleNum(self, graph):
        n = len(graph)
        dsu = DSU(n)

        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    dsu.union(i, j)

        return len(set([dsu.find(i) for i in range(n)]))

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
