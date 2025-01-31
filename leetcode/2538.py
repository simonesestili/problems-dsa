class Solution:
    def maxOutput(self, n, edges, price):
        graph = defaultdict(list)
        for a, b in edges: graph[a].append(b); graph[b].append(a)

        @cache
        def dfs(node, parent=-1):
            return price[node] + max((dfs(child, node) for child in graph[node] if child != parent), default=0)

        return max(dfs(i) - price[i] for i in range(n))
