class Solution:
    def minimumScore(self, nums, edges):
        n, graph, xors = len(nums), defaultdict(list), [0] * len(nums)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        def dfs(node):
            xors[node] = nums[node]
            seen.add(node)
            for neigh in graph[node]:
                if neigh in seen: continue
                dfs(neigh)
                xors[node] ^= xors[neigh]

        dfs(0)
        for i, (a, b) in enumerate(edges):
            for j, (c, d) in enumerate(edges):
                if i == j: continue
