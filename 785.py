class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        self.colors = [0] * n

        def dfs(node=0, col=-1):
            if self.colors[node]:
                return self.colors[node] == col
            self.colors[node] = col
            return all(dfs(neigh, col * -1) for neigh in graph[node])

        return all(self.colors[i] or dfs(i) for i in range(n))
