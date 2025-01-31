class Solution:
    def getAncestors(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges: graph[u].append(v)

        ans = [[] for _ in range(n)]
        def dfs(parent, curr):
            for ch in graph[curr]:
                if ans[ch] and ans[ch][-1] == parent: continue
                ans[ch].append(parent)
                dfs(parent, ch)

        for i in range(n): dfs(i, i)
        return ans

