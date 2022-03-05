class Solution:
    def getAncestors(self, n, edges):
        ans = [[] for _ in range(n)]
        graph = defaultdict(list)
        for u, v in edges: graph[u].append(v)

        def explore(parent, curr, seen):
            for j in graph[curr]:
                if j in seen: continue
                ans[j].append(parent)
                seen.add(j)
                explore(parent, j, seen)

        for i in range(n): explore(i, i, set([i]))
        return ans
