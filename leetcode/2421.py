class Solution:
    def numberOfGoodPaths(self, vals, edges):
        uf, graph = UF(len(vals)), defaultdict(list)
        for a, b in edges:
            if vals[a] < vals[b]: a, b = b, a
            graph[a].append(b)

        layers = defaultdict(list)
        for i, val in enumerate(vals): layers[val].append(i)

        ans = len(vals)
        for val in sorted(layers.keys()):
            for node in layers[val]:
                for child in graph[node]: uf.union(node, child)
            ans += sum(cnt * (cnt - 1) // 2 for cnt in Counter(map(uf.find, layers[val])).values())
        return ans

class UF:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, node):
        while self.parent[node] != node:
            node = self.parent[node]
        return node

    def union(self, a, b):
        ap, bp = self.find(a), self.find(b)
        if ap != bp: self.parent[ap] = bp
