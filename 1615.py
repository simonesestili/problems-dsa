class Solution:
    def maximalNetworkRank(self, n, roads):
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        best = -1
        for i in range(n):
            for j in range(i):
                best = max(best, len(graph[i]) + len(graph[j]) - (j in graph[i]))

        return best
