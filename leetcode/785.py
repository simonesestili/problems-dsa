class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        self.colors = [0] * n

        def dfs(node, col):
            if self.colors[node]:
                return self.colors[node] == col
            self.colors[node] = col
            return all(dfs(neigh, -col) for neigh in graph[node])

        return all(self.colors[i] or dfs(i, 1) for i in range(n))
