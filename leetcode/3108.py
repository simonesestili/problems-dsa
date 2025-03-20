class Solution:
    def minimumCost(self, n, edges, query):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        seen, groups = {}, []
        def dfs(u, group):
            for v, w in graph[u]:
                groups[group] = groups[group] & w if groups[group] != -1 else w
                if v not in seen:
                    seen[v] = group
                    dfs(v, group)

        for u in range(n):
            if u not in seen:
                seen[u] = len(groups)
                groups.append(-1)
                dfs(u, seen[u])

        return [groups[seen[s]] if seen[s] == seen[t] else -1 for s, t in query]
