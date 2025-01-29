class Solution:
    def findRedundantConnection(self, edges):
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]

class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, node):
        while self.reps[node] != node:
            node = self.reps[node]
        return node

    def union(self, u, v):
        urep, vrep = self.find(u), self.find(v)
        if urep == vrep:
            return False

        if self.ranks[urep] > self.ranks[vrep]:
            self.reps[vrep] = urep
            self.ranks[urep] += self.ranks[vrep]
        else:
            self.reps[urep] = vrep
            self.ranks[vrep] += self.ranks[urep]

        return True
