class DSU:
    def __init__(self):
        self.parent = {}
        self.ranks = {}

    def find(self, node):
        if node not in self.parent: return node
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, a, b):
        if a not in self.parent:
            self.parent[a] = a
            self.ranks[a] = 1
        if b not in self.parent:
            self.parent[b] = b
            self.ranks[b] = 1

        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.parent[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.parent[ap] = bp
                self.ranks[bp] += self.ranks[ap]

class Solution:
    def areSentencesSimilarTwo(self, s1, s2, pairs):
        if len(s1) != len(s2): return False

        dsu = DSU()
        [dsu.union(x, y) for x, y in pairs]

        for w1, w2 in zip(s1, s2):
            if w1 != w2 and dsu.find(w1) != dsu.find(w2):
                return False

        return True
