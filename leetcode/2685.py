class Solution:
    def countCompleteComponents(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen, comp = set(), set()
        def dfs(node):
            for ch in graph[node]:
                if ch not in comp:
                    comp.add(ch)
                    dfs(ch)

        ans = 0
        for i in range(n):
            if i not in seen:
                comp.add(i)
                dfs(i)
                ans += sum(len(graph[node]) for node in comp) == len(comp) * (len(comp) - 1)
                seen.update(comp)
                comp.clear()

        return ans
