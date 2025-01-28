class Solution:
    def eventualSafeNodes(self, graph):
        n, seen = len(graph), set()

        @cache
        def dfs(node):
            if node in seen:
                return False

            seen.add(node)
            return all(dfs(ch) for ch in graph[node])

        return [node for node in range(n) if dfs(node)]
