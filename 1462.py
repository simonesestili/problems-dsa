class Solution:
    def checkIfPrerequisite(self, n, reqs, queries):
        graph = defaultdict(list)
        for a, b in reqs: graph[b].append(a)

        def dfs(v, u):
            if 


        return [dfs(v, u) for u, v in queries]
