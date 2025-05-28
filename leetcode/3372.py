class Solution:
    def groups(self, graph, k):
        def dfs(node, seen, k):
            if k <= 0: return k == 0
            ans = 1
            for neigh in graph[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    ans += dfs(neigh, seen, k - 1)
            return ans

        return [dfs(node, set([node]), k) for node in range(len(graph))]

    def maxTargetNodes(self, edges1, edges2, k):
        graph1 = defaultdict(list)
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        graph2 = defaultdict(list)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        extra = max(self.groups(graph2, k - 1))
        return [cnt + extra for cnt in self.groups(graph1, k)]
