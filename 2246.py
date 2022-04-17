class Solution:
    def longestPath(self, parents, s):
        n, graph = len(parents),defaultdict(list)
        for node, parent in enumerate(parents):
            if parent != -1: graph[parent].append(node)

        cache = [0] * n
        def dfs(node):
            if not cache[node]:
                cache[node] = 1 + max((dfs(child) for child in graph[node] if s[node] != s[child]), default=0)
            return cache[node]

        [dfs(node) for node in range(n)]

        ans = 1
        for node in range(n):
            child_scores = [dfs(child) for child in graph[node] if s[child] != s[node]]
            ans = max(ans, 1 + sum(nlargest(2, child_scores)))

        return ans
