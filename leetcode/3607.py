class Solution:
    def processQueries(self, c, connections, queries):
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        groups = {}
        def dfs(node, group):
            if node in groups:
                return
            groups[node] = group
            for neigh in graph[node]:
                dfs(neigh, group)

        for i in range(1, c + 1):
            dfs(i, i)

        grids = defaultdict(list)
        for node, group in groups.items():
            grids[group].append(node)
        for nodes in grids.values():
            nodes.sort(reverse=True)

        ans, offline = [], set()
        for op, node in queries:
            if op == 2:
                offline.add(node)
                continue
            if node not in offline:
                ans.append(node)
                continue
            while grids[groups[node]] and grids[groups[node]][-1] in offline:
                grids[groups[node]].pop()
            ans.append(grids[groups[node]][-1] if grids[groups[node]] else -1)

        return ans
