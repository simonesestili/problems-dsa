class Solution:
    def countPairs(self, n, edges):
        dsu = DSU(n)
        for a, b in edges: dsu.union(a, b)

        ans = 0
        for i in range(n):
            ans += n - dsu.ranks[dsu.find(i)]

        return ans // 2

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
        if ap == bp: return
        if self.ranks[ap] > self.ranks[bp]:
            self.reps[bp] = ap
            self.ranks[ap] += self.ranks[bp]
        else:
            self.reps[ap] = bp
            self.ranks[bp] += self.ranks[ap]
