class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        res = 0

        shared = DSU(n)
        for _, u, v in filter(lambda e: e[0] == 3, edges):
            res += not shared.union(u - 1, v - 1)

        alice = DSU(n)
        alice.reps, alice.ranks = shared.reps[:], shared.ranks[:]
        for _, u, v in filter(lambda e: e[0] == 1, edges):
            res += not alice.union(u - 1, v - 1)

        bob = DSU(n)
        bob.reps, bob.ranks = shared.reps[:], shared.ranks[:]
        for _, u, v in filter(lambda e: e[0] == 2, edges):
            res += not bob.union(u - 1, v - 1)

        return res if alice.ranks[alice.find(0)] == bob.ranks[bob.find(0)] == n else -1

class DSU:
    def __init__(self, n):
        self.reps = list(range(n))
        self.ranks = [1] * n

    def find(self, a):
        while self.reps[a] != a:
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

