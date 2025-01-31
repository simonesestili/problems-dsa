class Solution:
    def longestCycle(self, edges):
        n = len(edges)
        self.mx, seen, dists, self.path = -1, set(), {}, 0

        def dfs(node):
            if node in seen: return
            if node in dists:
                self.mx = max(self.mx, self.path - dists[node])
            elif edges[node] != -1:
                dists[node] = self.path
                self.path += 1
                dfs(edges[node])
                self.path -= 1
                dists.pop
            seen.add(node)

        for i in range(n):
            dfs(i)
        return self.mx if self.mx else -1
