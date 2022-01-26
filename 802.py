class Solution:
    def eventualSafeNodes(self, graph):
        safe = [not bool(j) for j in graph]

        def dfs(i, seen):
            if safe[i] or i in seen: return safe[i]
            seen.add(i)
            safe[i] = all(dfs(j, seen) for j in graph[i])
            return safe[i]

        ans = []

        for i in range(len(graph)):
            dfs(i, set())
            if safe[i]:
                ans.append(i)

        return ans
