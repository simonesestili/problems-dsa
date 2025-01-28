class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        seen, prereqs = set(), [set() for _ in range(numCourses)]
        def dfs(i):
            if i in seen:
                return prereqs[i]

            seen.add(i)
            for ch in graph[i]:
                prereqs[i].add(ch)
                prereqs[i] |= dfs(ch)

            return prereqs[i]

        for i in range(numCourses):
            dfs(i)

        return [v in prereqs[u] for u, v in queries]
