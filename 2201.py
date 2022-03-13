class Solution:
    def digArtifacts(self, n, artifacts, dig):
        dsu, tiles = DSU(n*n), set()
        for r, c, rr, cc in artifacts:
            for i in range(r, rr + 1):
                for j in range(c, cc + 1):
                    dsu.union(n*r + c, n*i + j)
                    tiles.add((i, j))

        ans, counts = 0, defaultdict(int)
        for r, c in dig:
            if (r, c) not in tiles: continue
            parent = dsu.find(n*r + c)
            counts[parent] += 1
            ans += dsu.ranks[parent] == counts[parent]
        return ans

class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, node):
        while node != self.parents[node]:
            node = self.parents[node]
        return node

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp:
            if self.ranks[ap] > self.ranks[bp]:
                self.parents[bp] = ap
                self.ranks[ap] += self.ranks[bp]
            else:
                self.parents[ap] = bp
                self.ranks[bp] += self.ranks[ap]
