class Solution:
    def maxTargetNodes(self, edges1, edges2):
        graph1 = defaultdict(list)
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        graph2 = defaultdict(list)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        def dfs(graph, node, seen):
            for neigh in graph[node]:
                if neigh not in seen:
                    seen[neigh] = not seen[node]
                    dfs(graph, neigh, seen)

        dfs(graph1, 0, seen1 := {0: True})
        dfs(graph2, 0, seen2 := {0: True})

        groups = Counter(seen1.values())
        extra = max(Counter(seen2.values()).values())

        return [groups[seen1[i]] + extra for i in range(len(graph1))]
