class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        self.paths, self.path = [], []

        def dfs(node):
            self.path.append(node)
            if self.path[-1] == n - 1:
                self.paths.append(self.path[:])
            else:
                for child in graph[node]:
                    dfs(child)
            self.path.pop()

        dfs(0)
        return self.paths
