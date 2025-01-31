class Solution:
    def findMinHeightTrees(self, n, e):
        edges = defaultdict(list)
        for a, b in e:
            edges[a].append(b)
            edges[b].append(a)

        idx, self.parents, self.dists, self.seen = 0, [-1] * n, [-1] * n, set()
        def dfs(node=0, parent=-1, dist=0):
            if node in self.seen: return
            self.seen.add(node)
            self.parents[node], self.dists[node] = parent, dist
            for neigh in edges[node]:
                dfs(neigh, node, dist + 1)

        dfs()
        for i in range(n):
            idx = i if self.dists[i] > self.dists[idx] else idx

        self.parents, self.dists, self.seen = [-1] * n, [-1] * n, set()
        dfs(node=idx)
        idx = 0
        for i in range(n):
            idx = i if self.dists[i] > self.dists[idx] else idx
        
        slow, fast = idx, idx
        while True:
            if self.parents[fast] != -1 and self.parents[self.parents[fast]] == -1:
                return [slow, self.parents[slow]]
            elif self.parents[fast] == -1:
                return [slow]
            slow, fast = self.parents[slow], self.parents[self.parents[fast]]
