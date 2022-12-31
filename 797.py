class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        all_paths, curr_path = [], []

        def dfs(node):
            curr_path.append(node)
            if node == n - 1: all_paths.append(curr_path[:])
            else: [dfs(neigh) for neigh in graph[node]]
            curr_path.pop()

        dfs(0)
        return all_paths

